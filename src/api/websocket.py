from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from typing import Dict, Set
from uuid import UUID
from src.api.di.di import get_message_service, get_auth_service
from src.app.service.mesage_service import MessageService
from src.app.service.auth_service import AuthService

router = APIRouter(tags=["websocket"])


class ConnectionManager:
	def __init__(self):
		self.active_connections: Dict[UUID, Set[WebSocket]] = {}

	async def connect(self, websocket: WebSocket, room_id: UUID):
		await websocket.accept()
		self.active_connections.setdefault(room_id, set()).add(websocket)

	def disconnect(self, websocket: WebSocket, room_id: UUID):
		conns = self.active_connections.get(room_id)
		if not conns:
			return
		conns.discard(websocket)
		if not conns:
			self.active_connections.pop(room_id, None)

	async def broadcast(self, data: dict, room_id: UUID):
		for ws in list(self.active_connections.get(room_id, set())):
			try:
				await ws.send_json(data)
			except WebSocketDisconnect:
				# Клиент отключился «честно»
				self.disconnect(ws, room_id)
			except Exception:
				# Любая другая ошибка — тоже уничтожаем соединение
				self.disconnect(ws, room_id)


manager = ConnectionManager()


@router.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket,
                             room_id: UUID,
                             service: MessageService = Depends(get_message_service),
                             auth_service: AuthService = Depends(get_auth_service)
                             ):
	await manager.connect(websocket, room_id)
	try:
		while True:
			data: dict = await websocket.receive_json()
			raw_sender = data.get("sender")
			content = data.get("message")
			if not raw_sender or not content:
				await websocket.send_json({
					"error": "Both 'sender' and 'message' are required."
				})
				continue

			if raw_sender.startswith("anon_"):
				sender = raw_sender
			else:
				try:
					payload = auth_service.decode(raw_sender)
					sender = str(payload.get("sub", raw_sender))
					if sender is None:
						raise WebSocketDisconnect
				except Exception:
					await websocket.send_json({"error": "Invalid token."})
					raise WebSocketDisconnect
			service.save_message(sender=sender, content=content, room_id=room_id)
			await manager.broadcast(
					{"sender": sender, "message": content},
					room_id
				)
	except WebSocketDisconnect:
		manager.disconnect(websocket, room_id)
