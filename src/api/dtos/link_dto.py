from pydantic import BaseModel, HttpUrl, WebsocketUrl
from uuid import UUID


class CreateLinkRequest(BaseModel):
	url_origin: HttpUrl


class CreateLinkResponse(BaseModel):
	url_short: str


class GetUrlOriginResponse(BaseModel):
	url_origin: HttpUrl
	
class GetUrlOriginWithChatResponse(BaseModel):
	url_short: HttpUrl
	url_origin: HttpUrl
	ws: WebsocketUrl
	room_id: UUID
