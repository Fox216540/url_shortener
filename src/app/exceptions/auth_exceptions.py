from src.core.exceptions.exception import Error

LAYER  = "app/exceptions/auth_exceptions"

def get_message(message: str) -> str:
	return f"App: Auth_service\nLayer: {LAYER}\nMessage: {message}"

class InvalidCreateTokens(Error):
	"""Invalid Create Tokens"""
	message = "Invalid Create Tokens"
	def __init__(self):
		super().__init__(get_message(message=self.message))

class InvalidCreateAccessToken(Error):
	"""Invalid Create Access Token"""
	message = "Invalid Create Access Token"
	def __init__(self):
		super().__init__(get_message(message=self.message))

class InvalidDecode(Error):
	"""Invalid Decode"""
	message = "Invalid Decode"
	def __init__(self):
		super().__init__(get_message(message=self.message))

class InvalidDeleteRefresh(Error):
	"""Invalid Delete Refresh"""
	message = "Invalid Delete Refresh"
	def __init__(self):
		super().__init__(get_message(message=self.message))

class InvalidDeleteAllRefresh(Error):
	"""Invalid Delete All Refresh"""
	message = "Invalid Delete All Refresh"
	def __init__(self):
		super().__init__(get_message(message=self.message))

class InvalidExistsRefresh(Error):
	"""Invalid Exists Refresh"""
	message = "Invalid Exists Refresh"
	def __init__(self):
		super().__init__(get_message(message=self.message))