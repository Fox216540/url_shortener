from dataclasses import dataclass
from typing import Optional
from uuid import UUID


@dataclass
class Link:
	original_url: str
	short_code: Optional[str]
	room_id: Optional[UUID] = None
	id: Optional[int] = None
	alias: Optional[str] = None
	owner_id: Optional[UUID] = None

	@classmethod
	def from_orm(cls, orm_obj):
		return cls(
			id=orm_obj.id,
			original_url=orm_obj.original_url,
			owner_id=orm_obj.owner_id,
			alias=orm_obj.alias,
			short_code=orm_obj.short_code,
			room_id=orm_obj.room_id
		)
