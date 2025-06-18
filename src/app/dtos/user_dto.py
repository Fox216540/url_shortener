from dataclasses import dataclass
from src.domain.user.models.user import User
from src.domain.user.exceptions.user_exceptions import *
from src.domain.security.exceptions.token_storage_exception import *

@dataclass
class UserWithAccessToken(User):
	access_token: str = None


@dataclass
class UserWithTokens(UserWithAccessToken):
	refresh_token: str = None

ERRORS_SERVER_REPO = [
	InvalidCreateUser,
	InvalidGetUserByUsername,
	InvalidGetUserByEmail,
	InvalidGetUserById,
	UserNotExists,
	InvalidExistingUser,
	InvalidChangeUsername,
	InvalidChangeEmail,
	InvalidChangePassword,
	InvalidChangeName,
	InvalidDelete
]

ERRORS_SERVER_HASHER = [
	InvalidSaveRefreshToken,
	InvalidDeleteRefreshToken,
	InvalidDeleteAllRefreshTokens,
	InvalidExistsRefreshToken,
	RefreshTokenNotExists,
	RefreshTokensNotExist
]