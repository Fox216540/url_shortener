from src.core.exceptions.exception import Error

class JwtException(Error):
	def __init__(self, layer:str, message:str):
		message = f"Security: Jwt\nLayer: {layer}\nMessage: {message}"
		super().__init__(message)

class InvalidCreateAccessToken(JwtException):
	"""Invalid Create Access Token"""
	...

class InvalidCreateRefreshToken(JwtException):
	"""Invalid Create Refresh Token"""
	...

class InvalidDecode(JwtException):
	"""Invalid Decode"""
	...



