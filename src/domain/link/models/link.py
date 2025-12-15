from pydantic import BaseModel, HttpUrl
from uuid import UUID


class Link(BaseModel):
	original_url: HttpUrl
	short_code: str
	room_id: UUID | None = None
	id: int | None = None
	alias: str | None = None
	owner_id: UUID | None = None


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
