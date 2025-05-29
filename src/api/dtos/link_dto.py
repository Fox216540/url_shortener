from pydantic import BaseModel
from typing import Optional, List


class CreateLinkRequest(BaseModel):
    url_origin: Optional[str]


class CreateLinkResponse(BaseModel):
    url_short: Optional[str]


class GetUrlOriginResponse(BaseModel):
    url_origin: Optional[str]
