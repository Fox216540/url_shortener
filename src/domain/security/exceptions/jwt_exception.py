from src.core.exceptions.exception import Error

LAYER = "Domain/security/jwt"

class JwtException(Error):
	def __init__(self, layer:str, message:str, error:str):
		message = f"Security: Jwt\nLayer: {layer}\nMessage: {message}\nError: {error}"
		super().__init__(message)

class JwtServerException(JwtException):
	def __init__(self, layer:str, message:str):
		super().__init__(layer=layer, message=message, error="Server Error")

class InvalidCreateAccessToken(JwtServerException):
	"""Invalid Create Access Token"""
	...

class InvalidCreateRefreshToken(JwtServerException):
	"""Invalid Create Refresh Token"""
	...

class InvalidDecodeToken(JwtServerException):
	"""Invalid Decode"""
	...

class JwtNotFoundException(JwtException):
	def __init__(self, layer:str, message:str):
		super().__init__(layer=layer, message=message, error="Not Found Error")

class RefreshTokenNotFound(JwtNotFoundException):
	"""Refresh Token Not Found"""
	def __init__(self):
		super().__init__(layer=LAYER, message="Refresh Token Not Found")
	
