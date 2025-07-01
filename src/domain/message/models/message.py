from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class Message(BaseModel):
	room_id: UUID
	sender: str
	content: str
	id: UUID | None = None
	created_at: datetime | None = None
	it_is_me: bool = False

	@classmethod
	def check_it_is_me(cls, user_id: str | None, sender: str) -> bool:
		return user_id is not None and user_id == sender

	@classmethod
	def from_orm(cls, orm_obj, user_id: str | None = None):
		it_is_me = cls.check_it_is_me(user_id, orm_obj.sender)
		return cls(
			id=orm_obj.uuid_id,
			room_id=orm_obj.room_id,
			sender=orm_obj.sender,
			content=orm_obj.content,
			created_at=orm_obj.created_at,
			it_is_me=it_is_me,
		)
