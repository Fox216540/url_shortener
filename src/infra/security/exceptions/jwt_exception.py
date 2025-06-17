from src.domain.security.exceptions.jwt_exception import JwtException

LAYER  = "Infra/security/jwt"


class InvalidCreateAccessToken(JwtException):
	"""Invalid Create Access Token"""
	message = "Invalid Create Access Token"
	def __init__(self):
		super().__init__(layer=LAYER , message=self.message)

class InvalidCreateRefreshToken(JwtException):
	"""Invalid Create Refresh Token"""
	message = "Invalid Create Refresh Token"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InvalidDecode(JwtException):
	"""Invalid Decode"""
	message = "Invalid Decode"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

ERRORS_SERVER = [
	InvalidCreateAccessToken,
	InvalidCreateRefreshToken,
	InvalidDecode
]

ERRORS_ALL = ERRORS_SERVER
