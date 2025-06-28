from pydantic import BaseModel, HttpUrl


class CreateLinkRequest(BaseModel):
    url_origin: HttpUrl


class CreateLinkResponse(BaseModel):
    url_short: str


class GetUrlOriginResponse(BaseModel):
    url_origin: HttpUrl
