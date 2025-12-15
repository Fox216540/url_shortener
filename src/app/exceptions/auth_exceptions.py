from src.core.exceptions.exception import Error

LAYER  = "app/service/auth_service"


class AuthServiceException(Error):
	def __init__(self, message:str):
		message = f"App: Auth_service\nLayer: {LAYER}\nMessage: {message} Error: Server Error"
		super().__init__(message)


class InvalidCreateTokens(AuthServiceException):
	"""Invalid Create Tokens"""
	message = "Invalid Create Tokens"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidCreateAccessToken(AuthServiceException):
	"""Invalid Create Access Token"""
	message = "Invalid Create Access Token"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidDecode(AuthServiceException):
	"""Invalid Decode"""
	message = "Invalid Decode"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidDeleteRefresh(AuthServiceException):
	"""Invalid Delete Refresh"""
	message = "Invalid Delete Refresh"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidDeleteAllRefresh(AuthServiceException):
	"""Invalid Delete All Refresh"""
	message = "Invalid Delete All Refresh"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidExistsRefresh(AuthServiceException):
	"""Invalid Exists Refresh"""
	message = "Invalid Exists Refresh"
	def __init__(self):
		super().__init__(message=self.message)