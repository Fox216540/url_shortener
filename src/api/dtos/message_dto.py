from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class DeleteMessageResponse(BaseModel):
	message: str

class ChangeMessageRequest(BaseModel):
	new_content: str
	user_id: str | None = None

class ChangeMessageResponse(BaseModel):
	message: str


class DeleteMessageRequest(BaseModel):
	user_id: str | None = None

class MessageRequest(BaseModel):
	user_id: str

class MessageResponse(BaseModel):
	id: UUID
	content: str
	sender: str
	created_at: datetime
	it_is_me: bool = False


class WebSocketMessage(BaseModel):
	sender: str
	content: str