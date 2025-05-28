from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID

class CreateUserRequest(BaseModel):
    name: Optional[str]
    email: Optional[str]
    username: Optional[str]
    password: Optional[str]


class CreateUserResponse(BaseModel):
    uuid: Optional[UUID]
    message: Optional[str]


class GetUuidOfUserRequest(BaseModel):
    mail: Optional[str]
    password: Optional[str]


class GetUuidOfUserResponse(BaseModel):
    uuid: Optional[UUID]


class CreateUserLinkRequest(BaseModel):
    email: Optional[str]
    password: Optional[str]
    alias: Optional[str]
    original_url: Optional[str]


class CreateUserLinkResponse(BaseModel):
    url_short: Optional[str]