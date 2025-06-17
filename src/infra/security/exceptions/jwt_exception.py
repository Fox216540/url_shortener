from src.domain.security.exceptions.jwt_exception import (
InvalidCreateAccessToken,
InvalidCreateRefreshToken,
InvalidDecode
)

LAYER  = "Infra/security/jwt"


class InfraInvalidCreateAccessToken(InvalidCreateAccessToken):
	"""Invalid Create Access Token"""
	message = "Invalid Create Access Token"
	def __init__(self):
		super().__init__(layer=LAYER , message=self.message)

class InfraInvalidCreateRefreshToken(InvalidCreateRefreshToken):
	"""Invalid Create Refresh Token"""
	message = "Invalid Create Refresh Token"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraInvalidDecode(InvalidDecode):
	"""Invalid Decode"""
	message = "Invalid Decode"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

