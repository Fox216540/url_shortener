from fastapi import WebSocket, WebSocketDisconnect
from typing import Dict, Set
from uuid import UUID
from src.infra.websocket.exceptions import conn_manager_exception
from src.logger import error_logger


class ConnectionManager:
	def __init__(self):
		self.active_connections: Dict[UUID, Set[WebSocket]] = {}

	async def connect(self, websocket: WebSocket, room_id: UUID):
		try:
			await websocket.accept()
			self.active_connections.setdefault(room_id, set()).add(websocket)
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise conn_manager_exception.InvalidConnect() from e

	async def disconnect(self, websocket: WebSocket, room_id: UUID):
		if websocket.client_state.name == "CONNECTED":
			try:
				conns = self.active_connections.get(room_id)
				if conns and websocket in conns:
					conns.remove(websocket)
					if not conns:
						self.active_connections.pop(room_id)
				await websocket.close()
			except Exception as e:
				error_logger.error(f"{str(e)}", exc_info=True)
				raise conn_manager_exception.InvalidDisconnect() from e

	async def broadcast(self, data: dict, room_id: UUID):
		try:
			for ws in list(self.active_connections.get(room_id, set())):
				if ws.client_state.name == "CONNECTED":
					try:
						await ws.send_json(data)
					except WebSocketDisconnect:
						await self.disconnect(ws, room_id)
					except Exception:
						await self.disconnect(ws, room_id)
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise conn_manager_exception.InvalidBroadcast() from e
