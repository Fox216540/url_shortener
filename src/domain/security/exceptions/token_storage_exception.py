from src.core.exceptions.exception import Error

class TokenStorageException(Error):
	def __init__(self, layer:str, message:str):
		message = f"Security: Token storage\nLayer: {layer}\nMessage: {message}"
		super().__init__(message)

class InvalidSaveRefreshToken(TokenStorageException):
	"""Invalid Save Refresh Token"""
	...

class InvalidExistsRefreshToken(TokenStorageException):
	"""Invalid Create Refresh Token"""
	...

class InvalidDeleteRefreshToken(TokenStorageException):
	"""Invalid Delete Refresh Token"""
	...

class InvalidDeleteAllRefreshTokens(TokenStorageException):
	"""Invalid Delete All Refresh Tokens"""
	...

