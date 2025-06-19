from dataclasses import dataclass
from src.domain.user.models.user import User

@dataclass
class UserWithAccessToken(User):
	access_token: str = None


@dataclass
class UserWithTokens(UserWithAccessToken):
	refresh_token: str = None
