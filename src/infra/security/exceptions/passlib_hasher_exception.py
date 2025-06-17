from src.domain.security.exceptions.password_hasher_exception import PasswordHasherException

LAYER  = "Infra/security/user"


class InvalidHash(PasswordHasherException):
	"""Invalid Hash"""
	message = "Invalid Hash"
	def __init__(self):
		super().__init__(layer=LAYER , message=self.message)

class InvalidVerify(PasswordHasherException):
	"""Invalid Verify"""
	message = "Invalid Verify"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

ERRORS_SERVER = [
	InvalidHash,
	InvalidVerify
]

ERRORS_ALL = ERRORS_SERVER
