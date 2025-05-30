from fastapi import APIRouter, Request

from src.app.service.link_service import LinkService
from src.api.dtos.link_dto import (GetUrlOriginResponse,
                                   CreateLinkResponse,
                                   CreateLinkRequest
                                   )
from fastapi import Depends
from src.di.di import get_link_service
from settings import URL
from fastapi.responses import RedirectResponse
from typing import Optional
from src.logger import status_logger

router = APIRouter(tags=["link"])


@router.get("/{short_code}", response_model=GetUrlOriginResponse)
def get_original_link(request: Request, short_code: str, service: LinkService = Depends(get_link_service)):
    hostname = request.url.hostname
    username: Optional[str] = hostname.split(".")[0] if hostname and "." in hostname else None
    status_logger.info(username)
    url = service.get_url_by_short_code(short_code, username).original_url
    return RedirectResponse(url)


@router.post("/short", response_model=CreateLinkResponse)
def create_short_link(request: CreateLinkRequest, service: LinkService = Depends(get_link_service)):
    code = service.add_link(
        request.url_origin,
    ).short_code
    return CreateLinkResponse(url_short=f"{URL}/{code}")

# @router.post('/reg', response_model=)

