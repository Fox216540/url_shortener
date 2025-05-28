import logging
from abc import update_abstractmethods
from http import HTTPStatus
from http.client import HTTPException
from pyexpat.errors import messages

from fastapi import APIRouter, Response, HTTPException

from url_shortener.src.app.service.link_service import LinkService
from url_shortener.src.app.dtos.link_dto import (GetUrlOriginResponse,
                                                 CreateLinkResponse,
                                                 CreateLinkRequest
                                                 )
from fastapi import Depends
from url_shortener.src.app.di.di import get_service
from url_shortener.settings import URL
#from app.logger import logger

router = APIRouter(tags=["link"])


@router.get("/{short_code}", response_model=GetUrlOriginResponse)
def get_original_link(short_code: str, service: LinkService = Depends(get_service)):
    url = service.get_url_by_short_code(short_code)
    return GetUrlOriginResponse(url_origin=url)


@router.post("/short", response_model=CreateLinkResponse)
def create_short_link(request: CreateLinkRequest, service: LinkService = Depends(get_service)):
    short_code = service.add_link(
        request.url_origin,
    )

    return CreateLinkResponse(url_short=URL+short_code)

