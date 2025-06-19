from src.core.exceptions.exception import Error

LAYER  = "app/exceptions/link_exceptions"

def get_message(message: str) -> str:
	return f"App: Auth_service\nLayer: {LAYER}\nMessage: {message}"

class InvalidAddLink(Error):
	"""Invalid Add Link"""
	message = "Invalid Add Link"
	def __init__(self):
		super().__init__(get_message(message=self.message))

class InvalidGetUrlByShortCode(Error):
	"""Invalid Get Url By Short Code"""
	message = "InvalidGetUrlByShortCode"
	def __init__(self):
		super().__init__(get_message(message=self.message))

class InvalidGetAllLinksByOwnerId(Error):
	"""Invalid Get All Links By Owner ID"""
	message = "Invalid Get All Links By Owner Id"
	def __init__(self):
		super().__init__(get_message(message=self.message))

class InvalidDeleteLinkByOwnerId(Error):
	"""Invalid Delete Link By Owner Id"""
	message = "Invalid Delete Link By Owner Id"
	def __init__(self):
		super().__init__(get_message(message=self.message))

class InvalidDeleteAllByOwnerId(Error):
	"""Invalid Delete All By Owner ID"""
	message = "Invalid Delete All By Owner Id"
	def __init__(self):
		super().__init__(get_message(message=self.message))
