from fastapi import APIRouter
from fastapi import Request
from src.app.service.user_service import UserService
from src.api.dtos.user_dto import (
	CreateUserResponse,
	CreateUserRequest,
	CreateUserLinkRequest,
	CreateUserLinkResponse)
from fastapi import Depends
from uuid import UUID
from src.di.di import get_user_service
from src.api.success import success_message_create_user
from settings import URL

router = APIRouter(tags=["User"])


@router.post("/reg", response_model=CreateUserResponse)
def create_user(request: CreateUserRequest, service: UserService = Depends(get_user_service)):
	data = service.register_user(**request.dict())
	return CreateUserResponse(
		username=data.user.username,
		refresh_token=data.refresh_token,
		access_token=data.access_token,
		message=success_message_create_user
	)


@router.post("/create_link", response_model=CreateUserLinkResponse)
def create_link(request: CreateUserLinkRequest, raw_request: Request, service: UserService = Depends(get_user_service)):
	user_id = UUID(raw_request.state.user_id)
	username = raw_request.state.username
	# Передаём данные в сервис
	link = service.create_user_link(
		user_id=user_id,
		**request.dict()
	)
	short_identifier = link.alias or link.short_code
	return CreateUserLinkResponse(url_short=f"{username}.{URL}/{short_identifier}")
