from src.domain.security.exceptions.token_storage_exception import (
InvalidSaveRefreshToken,
InvalidDeleteRefreshToken,
InvalidDeleteAllRefreshTokens,
InvalidExistsRefreshToken,
RefreshTokensNotExist,
RefreshTokenNotExists
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

class InfraRefreshTokensNotExist(RefreshTokensNotExist):
	message = "Refresh Tokens Not Exist"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraRefreshTokenNotExists(RefreshTokenNotExists):
	message = "Refresh Token Not Exists"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)
