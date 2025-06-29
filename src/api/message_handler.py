from fastapi import APIRouter, Request
from typing import List
from datetime import datetime
from uuid import UUID
from src.app.service.mesage_service import MessageService
from src.app.service.websocket_service import WebsocketService
from src.api.dtos.message_dto import (
	DeleteMessageResponse, MessageResponse, ChangeMessageResponse,
	ChangeMessageRequest, DeleteMessageRequest
)
from src.api.exceptions.message_exceptions import UserIdNotExist
from fastapi import Depends
from src.api.di.di import get_message_service, get_connection_manager, get_error
from src.api.exceptions.error import Error
from src.api.dtos.success_message import *

router = APIRouter(tags=["message"], prefix="/m")

@router.delete("/{room_id}/{message_id}", response_model=DeleteMessageResponse)
async def delete_message(
		raw_request: Request,
		message_id: UUID,
		room_id: UUID,
		request: DeleteMessageRequest | None = None,
		service: MessageService = Depends(get_message_service),
		web_socket: WebsocketService = Depends(get_connection_manager),
		error: Error = Depends(get_error)
):
	try:
		user_id_from_state = getattr(raw_request.state, "user_id", None)
		user_id = None
		if user_id_from_state:
			user_id = user_id_from_state
		elif request:
			user_id = request.user_id
		else:
			raise UserIdNotExist()
		service.delete_message(message_id=message_id, user_id=user_id, room_id=room_id)
		await web_socket.broadcast(
			{"action": "delete", "message_id": str(message_id)},
			room_id=room_id
		)

		return DeleteMessageResponse(
			message=success_message_delete_message
		)
	except Exception as e:
		error.handle(e)


@router.get("/{room_id}", response_model=List[MessageResponse])
def get_history_of_chat(
		room_id: UUID,
		first_date: datetime,
		last_date: datetime,
		service: MessageService = Depends(get_message_service),
		error: Error = Depends(get_error)
):
	try:
		list_messages = service.get_messages_by_date(first_date, last_date, room_id)
		return [
			MessageResponse(
				id=message.id,
				content=message.content,
				sender=service.resolve_username(message.sender),
				created_at=message.created_at
			) for message in list_messages
		]
	except Exception as e:
		return error.handle(e)


@router.post("/{room_id}/{message_id}", response_model=ChangeMessageResponse)
async def change_message(
		raw_request: Request,
		request: ChangeMessageRequest,
		message_id: UUID,
		room_id: UUID,
		service: MessageService = Depends(get_message_service),
		web_socket: WebsocketService = Depends(get_connection_manager),
		error: Error = Depends(get_error)
):
	try:
		user_id_from_state = getattr(raw_request.state, "user_id", None)

		if user_id_from_state:
			user_id = user_id_from_state
		else:
			user_id = request.user_id
		new_message = service.change_message(
			user_id=user_id,
			room_id=room_id,
			new_content=request.new_content,
			message_id=message_id
		)

		await web_socket.broadcast(
			dict(action="change", message_id=str(new_message.id), new_content=new_message.content),
			room_id=room_id
		)

		return ChangeMessageResponse(message=success_message_change_message)
	except Exception as e:
		raise error.handle(e)

