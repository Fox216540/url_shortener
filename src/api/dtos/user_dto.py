from pydantic import BaseModel, EmailStr, Field, HttpUrl, WebsocketUrl

"""
USER REQUEST
"""


class LoginUserRequest(BaseModel):
	email_or_username: str = Field(..., min_length=5)
	password: str = Field(..., min_length=6)


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
	alias: str | None = None
	original_url: HttpUrl
	has_room: bool | None = None


"""
USER RESPONSE
"""


class UserResponse(BaseModel):
	username: str | None = None
	message: str


class UserWithAccessTokenResponse(UserResponse):
	access_token: str


class ExistResponse(BaseModel):
	msg: str
	exist: bool


class CreateUserLinkResponse(BaseModel):
	url_short: str
	web_socket: WebsocketUrl | None = None


class UsersLinksResponse(BaseModel):
	url_short: str
	link: HttpUrl
