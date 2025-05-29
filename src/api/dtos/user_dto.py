from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID


class CreateUserRequest(BaseModel):
    name: Optional[str]
    email: Optional[str]
    username: Optional[str]
    password: Optional[str]


class CreateUserResponse(BaseModel):
    username: Optional[str]
    access_token: Optional[str]
    refresh_token: Optional[str]
    message: Optional[str]


class GetUuidOfUserRequest(BaseModel):
    mail: Optional[str]
    password: Optional[str]


class GetUuidOfUserResponse(BaseModel):
    uuid: Optional[UUID]


class CreateUserLinkRequest(BaseModel):
    alias: Optional[str] = None
    original_url: Optional[str]


class CreateUserLinkResponse(BaseModel):
    url_short: Optional[str]