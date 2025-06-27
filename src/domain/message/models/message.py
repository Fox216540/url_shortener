from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class Message(BaseModel):
    room_id: UUID
    sender: str
    content: str
    id: UUID | None = None
    created_at: datetime | None = None

    @classmethod
    def from_orm(cls, orm_obj):
        return cls(
            id=orm_obj.uuid_id,
            room_id=orm_obj.room_id,
            sender=orm_obj.sender,
            content=orm_obj.content,
            created_at=orm_obj.created_at,
        )
