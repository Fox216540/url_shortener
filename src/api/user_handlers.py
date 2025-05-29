from fastapi import APIRouter
from fastapi import Request
from src.app.service.user_service import UserService
from src.api.dtos.user_dto import *
from fastapi import Depends
from uuid import UUID
from src.di.di import get_user_service
from src.api.success import success_message_create_user
from settings import URL
from src.logger import status_logger
router = APIRouter(tags=["User"])


@router.post("/reg", response_model=UserResponse)
def create_user(request: CreateUserRequest, service: UserService = Depends(get_user_service)):
	data = service.register_user(**request.dict())
	return UserResponse(
		username=data.user.username,
		refresh_token=data.refresh_token,
		access_token=data.access_token,
		message=success_message_create_user
	)


@router.post("/create_link", response_model=CreateUserLinkResponse)
def create_link(request: CreateUserLinkRequest, raw_request: Request, service: UserService = Depends(get_user_service)):
	user_id = UUID(raw_request.state.user_id)
	username = raw_request.state.username
	link = service.create_user_link(
		user_id=user_id,
		**request.dict()
	)
	short_identifier = link.alias or link.short_code
	return CreateUserLinkResponse(url_short=f"{username}.{URL}/{short_identifier}")


@router.post("/change_password", response_model=UserResponse)
def change_password(
		request: ChangePasswordRequest,
		raw_request: Request,
		service: UserService = Depends(get_user_service)
	):
	user_id = UUID(raw_request.state.user_id)
	data = service.change_password(
		user_id=user_id,
		**request.dict()
	)

	return UserResponse(
		username=data.user.username,
		refresh_token=data.refresh_token,
		access_token=data.access_token,
		message=success_message_create_user
	)


@router.post("/change_username", response_model=UserResponse)
def change_username(
		request: ChangeUsernameRequest,
		raw_request: Request,
		service: UserService = Depends(get_user_service)
	):
	user_id = UUID(raw_request.state.user_id)
	data = service.change_username(
		user_id=user_id,
		**request.dict()
	)

	return UserResponse(
		username=data.user.username,
		refresh_token=data.refresh_token,
		access_token=data.access_token,
		message=success_message_create_user
	)


@router.post("/change_email", response_model=UserResponse)
def change_email(
		request: ChangeEmailRequest,
		raw_request: Request,
		service: UserService = Depends(get_user_service)
	):
	user_id = UUID(raw_request.state.user_id)
	data = service.change_email(
		user_id=user_id,
		**request.dict()
	)
	status_logger.info(data)
	return UserResponse(
		username=data.user.username,
		refresh_token=data.refresh_token,
		access_token=data.access_token,
		message=success_message_create_user
	)


@router.post("/change_name", response_model=UserResponse)
def change_name(
		request: ChangeNameRequest,
		raw_request: Request,
		service: UserService = Depends(get_user_service)
	):
	user_id = UUID(raw_request.state.user_id)
	data = service.change_name(
		user_id=user_id,
		**request.dict()
	)

	return UserResponse(
		username=data.user.username,
		refresh_token=data.refresh_token,
		access_token=data.access_token,
		message=success_message_create_user
	)
