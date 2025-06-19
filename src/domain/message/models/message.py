from dataclasses import dataclass
from typing import Optional
from uuid import UUID
from datetime import datetime


@dataclass
class Message:
    room_id: Optional[UUID]
    sender: Optional[str]
    content: Optional[str]
    id: Optional[UUID] = None
    created_at: Optional[datetime] = None

    @classmethod
    def from_orm(cls, orm_obj):
        return cls(
            id=orm_obj.uuid_id,
            room_id=orm_obj.room_id,
            sender=orm_obj.sender,
            content=orm_obj.content,
            created_at=orm_obj.created_at,
        )
