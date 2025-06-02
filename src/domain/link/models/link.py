from dataclasses import dataclass
from typing import Optional
from uuid import UUID
import base62

@dataclass
class Link:
	original_url: str
	id: Optional[int] = None
	alias: Optional[int] = None
	owner_id: Optional[UUID] = None

	@property
	def short_code(self) -> str:
		return base62.encode(self.id)

	@classmethod
	def from_orm(cls, orm_obj):
		return cls(
			id=orm_obj.id,
			original_url=orm_obj.original_url,
			owner_id=orm_obj.owner_id if orm_obj.owner_id else None,
			alias=orm_obj.alias
		)
