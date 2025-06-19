from src.domain.security.exceptions.password_hasher_exception import (
	InvalidHash,
	InvalidVerify
)

LAYER  = "Infra/security/user"


class InfraInvalidHash(InvalidHash):
	"""Invalid Hash"""
	message = "Invalid Hash"
	def __init__(self):
		super().__init__(layer=LAYER , message=self.message)

class InfraInvalidVerify(InvalidVerify):
	"""Invalid Verify"""
	message = "Invalid Verify"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

