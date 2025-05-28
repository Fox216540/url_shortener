from fastapi import APIRouter

from src.app.service.link_service import LinkService
from src.app.dtos.link_dto import (GetUrlOriginResponse,
                                   CreateLinkResponse,
                                   CreateLinkRequest
                                   )
from fastapi import Depends
from src.app.di.di import get_link_service
from settings import URL
from fastapi.responses import RedirectResponse
#from app.logger import logger

router = APIRouter(tags=["link"])


@router.get("/{short_code}", response_model=GetUrlOriginResponse)
def get_original_link(short_code: str, service: LinkService = Depends(get_link_service)):
    url = service.get_url_by_short_code(short_code).original_url
    return RedirectResponse(url)


@router.post("/short", response_model=CreateLinkResponse)
def create_short_link(request: CreateLinkRequest, service: LinkService = Depends(get_link_service)):
    code = service.add_link(
        request.url_origin,
    ).short_code
    return CreateLinkResponse(url_short=URL+code)

# @router.post('/reg', response_model=)

