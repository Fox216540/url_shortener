from fastapi import APIRouter, Request, Depends
from pydantic import HttpUrl, WebsocketUrl
from src.api.dtos.link_dto import (
	CreateLinkResponse, CreateLinkRequest,
	GetUrlOriginResponse, GetUrlOriginWithChatResponse
)
from src.api.di.di import get_link_service, get_user_service, get_error
from settings import URL
from src.app.service.link_service import LinkService
from src.app.service.user_service import UserService
from src.api.exceptions.error import Error

router = APIRouter(tags=["link"])

@router.get("/{short_code}", response_model=GetUrlOriginResponse)
def get_original_link(request: Request,
                      short_code: str,
                      link_service: LinkService = Depends(get_link_service),
                      user_service: UserService = Depends(get_user_service),
                      error: Error = Depends(get_error)):
	try:
		hostname = request.url.hostname
		user_id = None
		if hostname and "." in hostname:
			candidate = hostname.split(".")[0]
			user = user_service.get_user_by_username(candidate)
			if user and user.id:
				user_id = user.id
		url = link_service.get_url_by_short_code_or_alias(short_code, user_id).original_url
		return GetUrlOriginResponse(
			url_origin=url,
		)
	except Exception as e:
		return error.handle(e)

@router.get("/{short_code}/c", response_model=GetUrlOriginWithChatResponse)
def get_original_link_with_chat(
		request: Request,
		short_code: str,
		link_service: LinkService = Depends(get_link_service),
		user_service: UserService = Depends(get_user_service),
        error: Error = Depends(get_error)
):
	try:
		hostname = request.url.hostname
		candidate = hostname.split(".")[0]
		user = user_service.get_user_by_username(candidate)
		user_id = user.id
		username = user.username
		room_id = link_service.get_url_by_short_code_or_alias(short_code, user_id).room_id
		original_url = link_service.get_url_by_short_code_or_alias(short_code, user_id).original_url
		ws = WebsocketUrl(f"ws://{URL}/ws/{room_id}")
		return GetUrlOriginWithChatResponse(
			url_origin=original_url,
			ws=ws,
			url_short=HttpUrl(f"http://{username}.{URL}/{short_code}"),
			room_id=room_id
		)
	except Exception as e:
		error.handle(e)

@router.post("/short", response_model=CreateLinkResponse)
def create_short_link(request: CreateLinkRequest,
                      service: LinkService = Depends(get_link_service),
                      error: Error = Depends(get_error)):
	try:
		code = service.add_link(
			request.url_origin,
		).short_code
		return CreateLinkResponse(url_short=f"{URL}/{code}")
	except Exception as e:
		return error.handle(e)

