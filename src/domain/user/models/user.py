from pydantic import BaseModel
from uuid import UUID


class User(BaseModel):
    name: str
    email: str
    username: str
    password: str
    id: UUID | None = None

    @classmethod
    def from_orm(cls, orm_obj):
        return cls(
            id=orm_obj.uuid_id,
            name=orm_obj.name,
            email=orm_obj.email,
            username=orm_obj.username,
            password=orm_obj.password,
        )
