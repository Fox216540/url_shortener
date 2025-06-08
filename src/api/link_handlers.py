from fastapi import APIRouter, Request

from src.app.service.link_service import LinkService
from src.app.service.user_service import UserService
from src.api.dtos.link_dto import (GetUrlOriginResponse,
                                   CreateLinkResponse,
                                   CreateLinkRequest
                                   )
from fastapi import Depends
from src.api.di.di import get_link_service, get_user_service
from settings import URL
from fastapi.responses import RedirectResponse
from src.logger import status_logger

router = APIRouter(tags=["link"])


@router.get("/{short_code}", response_model=GetUrlOriginResponse)
def get_original_link(request: Request,
                      short_code: str,
                      service: LinkService = Depends(get_link_service),
                      user_service: UserService = Depends(get_user_service)):
	hostname = request.url.hostname
	user_id = None
	if hostname and "." in hostname:
		candidate = hostname.split(".")[0]
		user = user_service.get_user_by_username(candidate)
		if user and user.id:
			user_id = user.id
	status_logger.info(user_id)
	url = service.get_url_by_short_code(short_code, user_id).original_url
	return RedirectResponse(url)


@router.post("/short", response_model=CreateLinkResponse)
def create_short_link(request: CreateLinkRequest, service: LinkService = Depends(get_link_service)):
	code = service.add_link(
		request.url_origin,
	).short_code
	return CreateLinkResponse(url_short=f"{URL}/{code}")

# @router.post('/reg', response_model=)
