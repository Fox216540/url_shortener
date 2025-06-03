from typing import Optional
from pydantic import BaseModel, EmailStr, Field


"""
USER REQUEST
"""


class CreateUserRequest(BaseModel):
	name: str = Field(..., min_length=1)
	email: EmailStr
	username: str = Field(..., min_length=5, max_length=32)
	password: str = Field(..., min_length=6)


class ChangeNameRequest(BaseModel):
	name: str = Field(..., min_length=1)


class ChangeEmailRequest(BaseModel):
	email: EmailStr


class ChangeUsernameRequest(BaseModel):
	username: str = Field(..., min_length=5, max_length=32)


class ChangePasswordRequest(BaseModel):
	old_password: str = Field(..., min_length=6)
	new_password: str = Field(..., min_length=6)


class CreateUserLinkRequest(BaseModel):
	alias: Optional[str] = None
	original_url: str


"""
USER RESPONSE
"""


class UserResponse(BaseModel):
	username: str
	access_token: str
	refresh_token: str
	message: Optional[str] = None


class ExistResponse(BaseModel):
	msg: str
	exist: bool


class CreateUserLinkResponse(BaseModel):
	url_short: str


class UsersLinksResponse(BaseModel):
	url_short: str
	link: str
