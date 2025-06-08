from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID


class DeleteMessageResponse(BaseModel):
    message: Optional[str]


class DeleteMessageRequest(BaseModel):
    message_id: Optional[UUID]
    room_id: Optional[UUID]


# class GetUrlOriginResponse(BaseModel):
#     url_origin: Optional[str]
