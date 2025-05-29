from fastapi import APIRouter

from src.app.service.user_service import UserService
from src.app.dtos.user_dto import (
	CreateUserResponse,
	CreateUserRequest,
	GetUuidOfUserRequest,
	GetUuidOfUserResponse,
	CreateUserLinkRequest,
	CreateUserLinkResponse)
from fastapi import Depends

from src.app.di.di import get_user_service
from src.api.success import success_message_create_user
from src.logger import status_logger
from settings import URL

router = APIRouter(tags=["User"])


@router.post("/reg", response_model=CreateUserResponse)
def create_user(request: CreateUserRequest, service: UserService = Depends(get_user_service)):
	user = service.register_user(**request.dict())
	return CreateUserResponse(username=user.username, message=success_message_create_user)


@router.post("/create_link", response_model=CreateUserLinkResponse)
def create_link(request: CreateUserLinkRequest, service: UserService = Depends(get_user_service)):
	link = service.create_user_link(**request.dict())
	short_identifier = link.alias or link.short_code
	return CreateUserLinkResponse(url_short=f"{URL}/{short_identifier}")
