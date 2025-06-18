from src.domain.security.exceptions.jwt_exception import *
from src.domain.security.exceptions.token_storage_exception import *

ERRORS_SERVER_JWT = [
	InvalidCreateAccessToken,
	InvalidCreateRefreshToken,
	InvalidDecodeToken
]

ERRORS_SERVER_STORAGE = [
	InvalidSaveRefreshToken,
	InvalidDeleteRefreshToken,
	InvalidDeleteAllRefreshTokens,
	InvalidExistsRefreshToken,
	RefreshTokenNotExists,
	RefreshTokensNotExist
]

ERRORS_SERVER_ALL = ERRORS_SERVER_JWT + ERRORS_SERVER_STORAGE