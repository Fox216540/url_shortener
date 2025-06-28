from src.core.exceptions.exception import Error

LAYER  = "app/service/message_service"


class MessageServiceException(Error):
	def __init__(self, message:str):
		message = f"App: Message_service\nLayer: {LAYER}\nMessage: {message} Error: Server Error"
		super().__init__(message)


class InvalidSaveMessage(MessageServiceException):
	"""Invalid Save Message"""
	message = "Invalid Save Message"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidGetMessagesByDate(MessageServiceException):
	"""Invalid Get Messages By Date"""
	message = "Invalid Get Messages By Date"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidDeleteMessage(MessageServiceException):
	"""Invalid Delete Message"""
	message = "Invalid Delete Message"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidResolveUsername(MessageServiceException):
	"""Invalid Resolve Username"""
	message = "Invalid Resolve Username"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidChangeMessage(MessageServiceException):
	"""Invalid Change Message"""
	message = "Invalid Change Message"
	def __init__(self):
		super().__init__(message=self.message)
