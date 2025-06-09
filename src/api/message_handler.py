from fastapi import APIRouter, Request
import asyncio
from uuid import UUID
from src.app.service.mesage_service import MessageService
from src.app.service.websocket_service import WebsocketService
from src.api.dtos.message_dto import DeleteMessageResponse, DeleteMessageRequest
from fastapi import Depends
from src.api.di.di import get_message_service, get_connection_manager
from src.api.dtos.success_message import *

router = APIRouter(tags=["message"], prefix="/m")


@router.delete("/{room_id}/{message_id}", response_model=DeleteMessageResponse)
async def get_original_link(
		message_id: UUID,
        room_id: UUID,
        service: MessageService = Depends(get_message_service),
        web_socket: WebsocketService = Depends(get_connection_manager)
):
	delete = service.delete_message(message_id=message_id)
	if not delete:
		pass
	await web_socket.broadcast(
		{"action": "delete", "message_id": str(message_id)},
		room_id=room_id
	)

	return DeleteMessageResponse(
		message=success_message_delete_message
	)


# TODO: Поменять на изменение сообщения и добавить история
#
# @router.post("/short", response_model=CreateLinkResponse)
# def create_short_link(request: CreateLinkRequest, service: LinkService = Depends(get_link_service)):
# 	code = service.add_link(
# 		request.url_origin,
# 	).short_code
# 	return CreateLinkResponse(url_short=f"{URL}/{code}")

# @router.post('/reg', response_model=)
