from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from uuid import UUID
from src.api.di.di import get_message_service, get_auth_service, get_connection_manager, get_user_service
from src.app.service.websocket_service import WebsocketService
from src.app.service.mesage_service import MessageService
from src.app.service.auth_service import AuthService
from src.app.service.user_service import UserService
from src.logger import status_logger

router = APIRouter(tags=["websocket"])


@router.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket,
                             room_id: UUID,
                             service: MessageService = Depends(get_message_service),
                             auth_service: AuthService = Depends(get_auth_service),
                             manager: WebsocketService = Depends(get_connection_manager),
                             user_service: UserService = Depends(get_user_service)
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
				username = "anon"
			else:
				try:
					payload = auth_service.decode(raw_sender)
					sender_uuid = payload.get("sub", raw_sender)
					user = user_service.get_user_by_id(UUID(sender_uuid))
					sender = str(user.id)
					username = user.username
					if sender_uuid is None:
						raise Exception
				except Exception:
					await websocket.send_json({"error": "Invalid token."})
					raise WebSocketDisconnect
			message = service.save_message(sender=sender, content=content, room_id=room_id)
			await manager.broadcast(
					{"sender": username, "message": message.content, "message_id": str(message.id)},
					room_id
				)
	except WebSocketDisconnect:
		await manager.disconnect(websocket, room_id)
