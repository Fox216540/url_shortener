from fastapi import APIRouter, Request
from typing import List
from datetime import datetime
from uuid import UUID
from src.app.service.mesage_service import MessageService
from src.app.service.websocket_service import WebsocketService
from src.api.dtos.message_dto import DeleteMessageResponse, MessageResponse, ChangeMessageResponse
from fastapi import Depends
from src.api.di.di import get_message_service, get_connection_manager
from src.api.dtos.success_message import *

router = APIRouter(tags=["message"], prefix="/m")


@router.delete("/{room_id}/{message_id}", response_model=DeleteMessageResponse)
async def delete_message(
		raw_request: Request,
		message_id: UUID,
		room_id: UUID,
		user_id: str = None,
		service: MessageService = Depends(get_message_service),
		web_socket: WebsocketService = Depends(get_connection_manager)
):
	user_id_from_state = getattr(raw_request.state, "user_id", None)
	if user_id_from_state:
		user_id = user_id_from_state

	if not user_id:
		raise Exception

	delete = service.delete_message(message_id=message_id, user_id=user_id, room_id=room_id)
	if not delete:
		pass
	await web_socket.broadcast(
		{"action": "delete", "message_id": str(message_id)},
		room_id=room_id
	)

	return DeleteMessageResponse(
		message=success_message_delete_message
	)


@router.get("/{room_id}", response_model=List[MessageResponse])
def get_history_of_chat(
		room_id: UUID,
		first_date: datetime,
		last_date: datetime,
		service: MessageService = Depends(get_message_service)
):
	list_messages = service.get_messages_by_date(first_date, last_date, room_id)
	return [
		MessageResponse(
			id=message.id,
			content=message.content,
			sender=service.resolve_username(message.sender),
			created_at=message.created_at
		) for message in list_messages
	]


@router.post("/{room_id}/{message_id}", response_model=ChangeMessageResponse)
async def change_message(
		raw_request: Request,
		message_id: UUID,
		room_id: UUID,
		new_content: str,
		user_id: str = None,
		service: MessageService = Depends(get_message_service),
		web_socket: WebsocketService = Depends(get_connection_manager)
):
	user_id_from_state = getattr(raw_request.state, "user_id", None)

	if user_id_from_state:
		user_id = user_id_from_state

	if not user_id:
		raise Exception

	new_message = service.change_message(
		user_id=user_id,
		room_id=room_id,
		new_content=new_content,
		message_id=message_id
	)

	if not new_message:
		raise Exception

	await web_socket.broadcast(
		{"action": "change", "message_id": str(new_message.id)},
		room_id=room_id
	)

	return ChangeMessageResponse(message=success_message_change_message)

#
# @router.post("/short", response_model=CreateLinkResponse)
# def create_short_link(request: CreateLinkRequest, service: LinkService = Depends(get_link_service)):
# 	code = service.add_link(
# 		request.url_origin,
# 	).short_code
# 	return CreateLinkResponse(url_short=f"{URL}/{code}")

# @router.post('/reg', response_model=)
