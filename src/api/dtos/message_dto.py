from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class DeleteMessageResponse(BaseModel):
	message: str


class ChangeMessageResponse(BaseModel):
	message: str


class DeleteMessageRequest(BaseModel):
	message_id: UUID
	room_id: UUID


class MessageResponse(BaseModel):
	id: UUID
	content: str
	sender: str
	created_at: datetime
