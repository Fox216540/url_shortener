from src.domain.user.models.user import User

class UserWithAccessToken(User):
	access_token: str

class UserWithTokens(UserWithAccessToken):
	refresh_token: str
