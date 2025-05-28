from sqlalchemy import Column, Integer, String
from src.infra.repositories.models.base import Base
import uuid


class UserORM(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid_id = Column(String(36), default=lambda: str(uuid.uuid4()), unique=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)


