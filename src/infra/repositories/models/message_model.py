from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from src.infra.repositories.models.base import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class MessageORM(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid_id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    room_id = Column(UUID(as_uuid=True), nullable=False)
    sender = Column(String(64), nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)


