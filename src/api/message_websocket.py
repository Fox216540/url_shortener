from fastapi import APIRouter, WebSocket, Depends
from uuid import UUID
from pydantic import ValidationError
from src.api.dtos.message_dto import WebSocketMessage
from src.api.di.di import get_message_service, get_auth_service, get_connection_manager, get_user_service, get_error
from src.app.service.websocket_service import WebsocketService
from src.app.service.mesage_service import MessageService
from src.app.service.auth_service import AuthService
from src.app.service.user_service import UserService
from src.api.exceptions.error import Error

router = APIRouter(tags=["websocket"])


@router.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket,
                             room_id: UUID,
                             service: MessageService = Depends(get_message_service),
                             auth_service: AuthService = Depends(get_auth_service),
                             manager: WebsocketService = Depends(get_connection_manager),
                             user_service: UserService = Depends(get_user_service),
                             error: Error = Depends(get_error)):
	await manager.connect(websocket, room_id)
	try:
		while True:
			try:
				data = await websocket.receive_json()
				message = WebSocketMessage(**data)
				if message.sender.startswith("anon_"):
					sender = message.sender
					username = "anon"
				else:
					try:
						payload = auth_service.decode(message.sender)
						sender_uuid = payload.get("sub", message.sender)
						user = user_service.get_user_by_id(UUID(sender_uuid))
						sender = str(user.id)
						username = user.username
					except Exception as e:
						await websocket.send_json({"error": "Invalid token."})
						await manager.disconnect(websocket, room_id)
						raise e
				message = service.save_message(sender=sender, content=message.content, room_id=room_id)
				await manager.broadcast(
						{"sender": username, "message": message.content, "message_id": str(message.id)},
						room_id
					)
			except ValidationError:
				await websocket.send_json({
						"error": "Both 'sender' and 'content' are required."
					})
				await manager.disconnect(websocket, room_id)
				break
			except Exception as e:
					if websocket.client_state.name == "DISCONNECTED":
						# Клиент уже отключён, повторно disconnect не вызываем
						break
					try:
						await manager.disconnect(websocket, room_id)
					except Exception:
						# Игнорируем ошибку повторного disconnect
						pass
					raise e
	except Exception as e:
		error.handle(e)
