from src.infra.repositories.models.base import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint


class LinkORM(Base):
	__tablename__ = 'links'

	id = Column(Integer, autoincrement=True, primary_key=True)
	original_url = Column(String, nullable=False)
	alias = Column(String)
	owner_id = Column(String, nullable=True)

	__table_args__ = (
		UniqueConstraint('owner_id', 'alias', name='uix_username_alias'),
	)

