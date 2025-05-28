from sqlalchemy import Column, Integer, String
from src.infra.repositories.models.base import Base


class LinkORM(Base):
    __tablename__ = 'links'

    id = Column(Integer, autoincrement=True, primary_key=True)
    original_url = Column(String, nullable=False)
    owner_id = Column(String, nullable=True)

