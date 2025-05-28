from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class LinkORM(Base):
    __tablename__ = 'links'

    id = Column(Integer, autoincrement=True, primary_key=True)
    original_url = Column(String)
    owner_id = Column(String, nullable=True)

