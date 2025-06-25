from src.core.exceptions.exception import Error

class TokenStorageException(Error):
	def __init__(self, layer:str, message:str, error:str):
		message = f"Security: Token storage\nLayer: {layer}\nMessage: {message}\nError: {error}"
		super().__init__(message)

class TokenStorageServerException(TokenStorageException):
	def __init__(self, layer:str, message:str):
		super().__init__(layer=layer, message=message, error="Server Error")

class TokenStorageNotFoundException(TokenStorageException):
	def __init__(self, layer:str, message:str):
		super().__init__(layer=layer, message=message, error="Not Found Error")

class InvalidSaveRefreshToken(TokenStorageServerException):
	"""Invalid Save Refresh Token"""
	...

class InvalidExistsRefreshToken(TokenStorageServerException):
	"""Invalid Create Refresh Token"""
	...

class InvalidDeleteRefreshToken(TokenStorageServerException):
	"""Invalid Delete Refresh Token"""
	...

class InvalidDeleteAllRefreshTokens(TokenStorageServerException):
	"""Invalid Delete All Refresh Tokens"""
	...

class RefreshTokensNotExist(TokenStorageNotFoundException):
	"""Refresh Tokens Don't Exist"""
	...

class RefreshTokenNotExists(TokenStorageNotFoundException):
	"""Refresh Token Doesn't Exist"""
	...

