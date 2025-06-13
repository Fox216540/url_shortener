from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class DeleteMessageResponse(BaseModel):
	message: Optional[str]


class ChangeMessageResponse(BaseModel):
	message: Optional[str]


class DeleteMessageRequest(BaseModel):
	message_id: Optional[UUID]
	room_id: Optional[UUID]


class MessageResponse(BaseModel):
	id: Optional[UUID]
	content: Optional[str]
	sender: Optional[str]
	created_at: Optional[datetime]
