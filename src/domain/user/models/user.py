from dataclasses import dataclass
from dataclasses import dataclass
from typing import Optional
from uuid import UUID


@dataclass
class User:
    name: Optional[str]
    mail: Optional[str]
    username: Optional[str]
    password: Optional[str]
    id: Optional[UUID] = None

    @classmethod
    def from_orm(cls, orm_obj):
        return cls(
            id=orm_obj.uuid_id,
            name=orm_obj.name,
            mail=orm_obj.mail,
            username=orm_obj.username,
            password=orm_obj.password,
        )
