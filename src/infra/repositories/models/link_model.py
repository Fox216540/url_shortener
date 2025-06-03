from src.infra.repositories.models.base import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey
import uuid
from sqlalchemy.dialects.postgresql import UUID


class LinkORM(Base):
	__tablename__ = 'links'

	id = Column(Integer, autoincrement=True, primary_key=True)
	original_url = Column(String, nullable=False)
	alias = Column(String)
	owner_id = Column(UUID(as_uuid=True), ForeignKey("users.uuid_id"), nullable=True)

	__table_args__ = (
		UniqueConstraint('owner_id', 'alias', name='uix_username_alias'),
	)

