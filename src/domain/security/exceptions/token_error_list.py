from src.domain.security.exceptions.token_storage_exception import *

ERRORS_SERVER = [
	InvalidSaveRefreshToken,
	InvalidDeleteRefreshToken,
	InvalidDeleteAllRefreshTokens,
	InvalidExistsRefreshToken,
]

ERRORS_NOT_FOUND = [
	RefreshTokenNotExists,
	RefreshTokensNotExist
]

ERRORS_TOKEN_STORAGE = ERRORS_SERVER + ERRORS_NOT_FOUND