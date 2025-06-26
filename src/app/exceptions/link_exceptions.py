from src.core.exceptions.exception import Error

LAYER  = "app/service/link_service"


class LinkException(Error):
	def __init__(self, message:str):
		message = f"App: Link_service\nLayer: {LAYER}\nMessage: {message} Error: Server Error"
		super().__init__(message)


class InvalidAddLink(LinkException):
	"""Invalid Add Link"""
	message = "Invalid Add Link"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidGetUrlByShortCode(LinkException):
	"""Invalid Get Url By Short Code"""
	message = "InvalidGetUrlByShortCode"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidGetAllLinksByOwnerId(LinkException):
	"""Invalid Get All Links By Owner ID"""
	message = "Invalid Get All Links By Owner Id"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidDeleteLinkByOwnerId(LinkException):
	"""Invalid Delete Link By Owner Id"""
	message = "Invalid Delete Link By Owner Id"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidDeleteAllByOwnerId(LinkException):
	"""Invalid Delete All By Owner ID"""
	message = "Invalid Delete All By Owner Id"
	def __init__(self):
		super().__init__(message=self.message)
