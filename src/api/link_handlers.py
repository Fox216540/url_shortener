from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from src.api.dtos.link_dto import (CreateLinkResponse,CreateLinkRequest)
from src.api.di.di import get_link_service, get_user_service, get_error
from settings import URL
from src.app.service.link_service import LinkService
from src.app.service.user_service import UserService
from src.api.exceptions.error import Error
from src.logger import status_logger

router = APIRouter(tags=["link"])

#TODO: Добавить обработку endpoint с /с чтобы передавалось room_id
#TODO: в message_handler есть функция с получением чата
@router.get("/{short_code}")
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
		status_logger.info(user_id)
		url = link_service.get_url_by_short_code_or_alias(short_code, user_id).original_url
		return RedirectResponse(str(url))
	except Exception as e:
		return error.handle(e)


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

