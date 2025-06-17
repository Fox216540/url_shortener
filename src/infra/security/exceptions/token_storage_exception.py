from src.domain.security.exceptions.token_storage_exception import (
InvalidSaveRefreshToken,
InvalidDeleteRefreshToken,
InvalidDeleteAllRefreshTokens,
InvalidExistsRefreshToken,
)

LAYER  = "Infra/security/token_storage"


class InfraInvalidSaveRefreshToken(InvalidSaveRefreshToken):
	message = "Invalid Save Refresh Token"
	def __init__(self):
		super().__init__(layer=LAYER , message=self.message)

class InfraInvalidExistsRefreshToken(InvalidExistsRefreshToken):
	message = "Invalid Create Refresh Token"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraInvalidDeleteRefreshToken(InvalidDeleteRefreshToken):
	message = "Invalid Delete Refresh Token"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraInvalidDeleteAllRefreshTokens(InvalidDeleteAllRefreshTokens):
	message = "Invalid Delete All Refresh Tokens"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

