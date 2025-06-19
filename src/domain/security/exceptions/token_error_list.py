from src.domain.security.exceptions.token_storage_exception import *

ERRORS_TOKEN_STORAGE = [
	InvalidSaveRefreshToken,
	InvalidDeleteRefreshToken,
	InvalidDeleteAllRefreshTokens,
	InvalidExistsRefreshToken,
	RefreshTokenNotExists,
	RefreshTokensNotExist
]