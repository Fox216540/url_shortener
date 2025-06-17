from src.domain.security.exceptions.token_storage_exception import TokenStorageException

LAYER  = "Infra/security/token_storage"


class InvalidSaveRefreshToken(TokenStorageException):
	"""Invalid Save Refresh Token"""
	message = "Invalid Save Refresh Token"
	def __init__(self):
		super().__init__(layer=LAYER , message=self.message)

class InvalidExistsRefreshToken(TokenStorageException):
	"""Invalid Create Refresh Token"""
	message = "Invalid Create Refresh Token"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InvalidDeleteRefreshToken(TokenStorageException):
	"""Invalid Delete Refresh Token"""
	message = "Invalid Delete Refresh Token"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InvalidDeleteAllRefreshTokens(TokenStorageException):
	"""Invalid Delete All Refresh Tokens"""
	message = "Invalid Delete All Refresh Tokens"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

ERRORS_SERVER = [
	InvalidSaveRefreshToken,
	InvalidExistsRefreshToken,
	InvalidDeleteRefreshToken,
	InvalidDeleteAllRefreshTokens
]

ERRORS_ALL = ERRORS_SERVER
