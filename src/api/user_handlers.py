from fastapi import APIRouter
from fastapi import Request
from src.app.service.user_service import UserService
from src.app.service.link_service import LinkService
from src.api.dtos.user_dto import *
from fastapi import Depends
from uuid import UUID
from src.app.di.di import get_user_service, get_link_service
from src.api.dtos.success import *
from settings import URL
from src.logger import status_logger
from typing import List

router = APIRouter(tags=["User"], prefix='/user')

#TODO: Добавить logout и помещение refresh в куки
@router.post("/reg", response_model=UserResponse)
def create_user(request: CreateUserRequest, service: UserService = Depends(get_user_service)):
	data = service.register_user(**request.dict())
	return UserResponse(
		username=data.user.username,
		refresh_token=data.refresh_token,
		access_token=data.access_token,
		message=success_message_create_user
	)


@router.post("/create-link", response_model=CreateUserLinkResponse)
def create_link(request: CreateUserLinkRequest, raw_request: Request, service: UserService = Depends(get_user_service)):
	user_id = UUID(raw_request.state.user_id)
	username = raw_request.state.username
	link = service.create_user_link(
		user_id=user_id,
		**request.dict()
	)
	short_identifier = link.alias or link.short_code
	return CreateUserLinkResponse(
		url_short=f"{username}.{URL}/{short_identifier}"
	)


@router.post("/change-password", response_model=UserResponse)
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
		message=success_message_change_password
	)


@router.post("/change-username", response_model=UserResponse)
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
		message=success_message_change_username
	)


@router.post("/change-email", response_model=UserResponse)
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
		message=success_message_change_email
	)


@router.post("/change-name", response_model=UserResponse)
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
		message=success_message_change_name
	)


@router.get("/check-username", response_model=ExistResponse)
def check_username(username: str, service: UserService = Depends(get_user_service)):
	check = service.exist_username(username)
	if check:
		return ExistResponse(
			msg=success_message_exist_username,
			exist=check
		)
	return ExistResponse(
		msg=success_message_not_exist_username,
		exist=check
	)


@router.get("/check-email", response_model=ExistResponse)
def check_email(email: str, service: UserService = Depends(get_user_service)):
	check = service.exist_email(email)
	if check:
		return ExistResponse(
			msg=success_message_exist_email,
			exist=check
		)
	return ExistResponse(
		msg=success_message_not_exist_email,
		exist=check
	)


@router.post("/my-links", response_model=List[UsersLinksResponse])
def get_all_links(
		raw_request: Request,
		service: LinkService = Depends(get_link_service)
):
	username = raw_request.state.username
	user_id = UUID(raw_request.state.user_id)
	links = service.get_all_links_by_user_id(user_id)
	return [UsersLinksResponse(url_short=f"{username}.{URL}/{link.alias if link.alias else link.short_code}",
	                           link=link.original_url) for link in links]


@router.post("/refresh-tokens", response_model=UserResponse)
def refresh_tokens(
		request: Request,
		service: UserService = Depends(get_user_service)
):
	refresh_token = request.cookies.get("refresh_token")
	data = service.refresh_tokens(refresh_token)
	return UserResponse(
		username=data.user.username,
		refresh_token=data.refresh_token,
		access_token=data.access_token,
		message=success_message_update_tokens
	)