from fastapi import APIRouter
from fastapi import Request
from src.app.service.user_service import UserService
from src.app.service.link_service import LinkService
from src.api.dtos.user_dto import *
from fastapi import Depends
from uuid import UUID
from src.app.di.di import get_user_service, get_link_service
from src.api.dtos.success import *
from settings import URL, BUFFER_SECONDS, REFRESH_TOKEN_TIME
from typing import List
from fastapi.responses import JSONResponse

router = APIRouter(tags=["User"], prefix='/user')

"""
В планах: logout_all, delete_user
"""


@router.post("/reg", response_model=UserWithAccessTokenResponse)
def create_user(request: CreateUserRequest, service: UserService = Depends(get_user_service)):
	user = service.register_user(**request.dict())

	response_data = UserWithAccessTokenResponse(
		username=user.username,
		access_token=user.access_token,
		message=success_message_create_user
	)

	response = JSONResponse(content=response_data.dict())

	response.set_cookie(
		key="refresh_token",
		value=user.refresh_token,
		httponly=True,
		samesite="lax",
		path="/",
		max_age=REFRESH_TOKEN_TIME - BUFFER_SECONDS
	)
	return response


@router.post("/login", response_model=UserWithAccessTokenResponse)
def login_user(request: LoginUserRequest, service: UserService = Depends(get_user_service)):
	user = service.login_user(**request.dict())

	response_data = UserWithAccessTokenResponse(
		username=user.username,
		access_token=user.access_token,
		message=success_message_login_user
	)

	response = JSONResponse(content=response_data.dict())

	response.set_cookie(
		key="refresh_token",
		value=user.refresh_token,
		httponly=True,
		samesite="lax",
		path="/",
		max_age=REFRESH_TOKEN_TIME - BUFFER_SECONDS
	)

	return response


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
	user = service.change_password(
		user_id=user_id,
		**request.dict()
	)

	return UserResponse(
		username=user.username,
		message=success_message_change_password
	)


@router.post("/change-username", response_model=UserWithAccessTokenResponse)
def change_username(
		request: ChangeUsernameRequest,
		raw_request: Request,
		service: UserService = Depends(get_user_service)
):
	user_id = UUID(raw_request.state.user_id)
	user = service.change_username(
		user_id=user_id,
		**request.dict()
	)

	return UserWithAccessTokenResponse(
		username=user.username,
		access_token=user.access_token,
		message=success_message_change_username
	)


@router.post("/change-email", response_model=UserResponse)
def change_email(
		request: ChangeEmailRequest,
		raw_request: Request,
		service: UserService = Depends(get_user_service)
):
	user_id = UUID(raw_request.state.user_id)
	user = service.change_email(
		user_id=user_id,
		**request.dict()
	)
	# status_logger.info(data)
	return UserResponse(
		username=user.username,
		message=success_message_change_email
	)


@router.post("/change-name", response_model=UserResponse)
def change_name(
		request: ChangeNameRequest,
		raw_request: Request,
		service: UserService = Depends(get_user_service)
):
	user_id = UUID(raw_request.state.user_id)
	user = service.change_name(
		user_id=user_id,
		**request.dict()
	)

	return UserResponse(
		username=user.username,
		message=success_message_change_name
	)


@router.get("/check-username", response_model=ExistResponse)
def check_username(username: str, service: UserService = Depends(get_user_service)):
	check = service.exists_username(username)
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
	check = service.exists_email(email)
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
	links = service.get_all_links_by_owner_id(user_id)
	return [UsersLinksResponse(url_short=f"{username}.{URL}/{link.alias if link.alias else link.short_code}",
	                           link=link.original_url) for link in links]


@router.post("/refresh-tokens", response_model=UserWithAccessTokenResponse)
def refresh_tokens(
		request: Request,
		service: UserService = Depends(get_user_service)
):
	refresh_token = request.cookies.get("refresh_token")
	user = service.refresh_tokens(refresh_token)
	response_data = UserWithAccessTokenResponse(
		username=user.username,
		access_token=user.access_token,
		message=success_message_update_tokens
	)

	response = JSONResponse(content=response_data.dict())

	response.set_cookie(
		key="refresh_token",
		value=user.refresh_token,
		httponly=True,
		samesite="lax",
		path="/",
		max_age=REFRESH_TOKEN_TIME - BUFFER_SECONDS
	)

	return response


@router.post("/logout", response_model=UserResponse)
def refresh_tokens(
		request: Request,
		service: UserService = Depends(get_user_service)
):
	refresh_token = request.cookies.get("refresh_token")
	if not refresh_token:
		pass
	logout_status = service.logout_user(refresh_token)
	if logout_status:
		response_data = UserResponse(message=success_message_logout_user)
		response = JSONResponse(content=response_data.dict())
		response.delete_cookie(key="refresh_token")
		return response


@router.post("/logout_all", response_model=UserResponse)
def refresh_tokens(
		request: Request,
		service: UserService = Depends(get_user_service)
):
	refresh_token = request.cookies.get("refresh_token")
	if not refresh_token:
		pass
	logout_status = service.logout_all_user(refresh_token)
	if logout_status:
		response_data = UserResponse(message=success_message_logout_all_user)
		response = JSONResponse(content=response_data.dict())
		response.delete_cookie(key="refresh_token")
		return response


@router.delete("/link/{identifier}", response_model=UserResponse)
def delete_link(
		raw_request: Request,
        identifier: str,
        service: UserService = Depends(get_user_service)
):
	username = raw_request.state.username
	user_id = UUID(raw_request.state.user_id)
	if service.delete_link_by_user(user_id=user_id, identifier=identifier):
		return UserResponse(
			username=username,
			message=success_message_delete_link
		)


@router.delete("/links", response_model=UserResponse)
def delete_link(
		raw_request: Request,
        service: UserService = Depends(get_user_service)
):
	username = raw_request.state.username
	user_id = UUID(raw_request.state.user_id)
	if service.delete_all_user(user_id=user_id):
		return UserResponse(
			username=username,
			message=success_message_delete_links
		)
