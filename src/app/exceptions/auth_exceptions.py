from src.core.exceptions.exception import Error

LAYER  = "app/service/auth_exceptions"


class AuthException(Error):
	def __init__(self, message:str):
		message = f"App: Auth_service\nLayer: {LAYER}\nMessage: {message} Error: Server Error"
		super().__init__(message)


class InvalidCreateTokens(AuthException):
	"""Invalid Create Tokens"""
	message = "Invalid Create Tokens"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidCreateAccessToken(AuthException):
	"""Invalid Create Access Token"""
	message = "Invalid Create Access Token"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidDecode(AuthException):
	"""Invalid Decode"""
	message = "Invalid Decode"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidDeleteRefresh(AuthException):
	"""Invalid Delete Refresh"""
	message = "Invalid Delete Refresh"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidDeleteAllRefresh(AuthException):
	"""Invalid Delete All Refresh"""
	message = "Invalid Delete All Refresh"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidExistsRefresh(AuthException):
	"""Invalid Exists Refresh"""
	message = "Invalid Exists Refresh"
	def __init__(self):
		super().__init__(message=self.message)