from sqlalchemy import Column, Integer, String
from src.infra.repositories.models.base import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class UserORM(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid_id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)


