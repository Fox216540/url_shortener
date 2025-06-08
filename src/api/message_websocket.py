from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from uuid import UUID
from src.api.di.di import get_message_service, get_auth_service, get_connection_manager
from src.infra.websocket.connection_manager import ConnectionManager
from src.app.service.mesage_service import MessageService
from src.app.service.auth_service import AuthService

router = APIRouter(tags=["websocket"])


@router.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket,
                             room_id: UUID,
                             service: MessageService = Depends(get_message_service),
                             auth_service: AuthService = Depends(get_auth_service),
                             manager: ConnectionManager = Depends(get_connection_manager)
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
		await manager.disconnect(websocket, room_id)
