from pydantic import BaseModel
from typing import Optional, List


class CreateUserRequest(BaseModel):
    name: Optional[str]
    mail: Optional[str]
    username: Optional[str]
    password: Optional[str]


class CreateUserResponse(BaseModel):
    message: Optional[str]


class GetUuidOfUserRequest(BaseModel):
    mail: Optional[str]
    password: Optional[str]


class GetUuidOfUserResponse(BaseModel):
    uuid: Optional[str]
