from fastapi import WebSocket, WebSocketDisconnect
from typing import Dict, Set
from uuid import UUID


class ConnectionManager:
	def __init__(self):
		self.active_connections: Dict[UUID, Set[WebSocket]] = {}

	async def connect(self, websocket: WebSocket, room_id: UUID):
		await websocket.accept()
		self.active_connections.setdefault(room_id, set()).add(websocket)

	async def disconnect(self, websocket: WebSocket, room_id: UUID):
		conns = self.active_connections.get(room_id)
		if not conns:
			return
		try:
			conns.remove(websocket)
		except ValueError:
			pass
		try:
			await websocket.close()
		except Exception:
			pass

		if not conns:
			self.active_connections.pop(room_id, None)

	async def broadcast(self, data: dict, room_id: UUID):
		for ws in list(self.active_connections.get(room_id, set())):
			try:
				await ws.send_json(data)
			except WebSocketDisconnect:
				await self.disconnect(ws, room_id)
			except Exception:
				await self.disconnect(ws, room_id)
