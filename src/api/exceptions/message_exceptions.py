from src.core.exceptions.exception import Error

LAYER  = "api/message_handler"


class MessageHandlerException(Error):
	def __init__(self, message:str):
		message = f"Api: Message_handler\nLayer: {LAYER}\nMessage: {message} Error: Not Found"
		super().__init__(message)


class UserIdNotExist(MessageHandlerException):
	"""User ID not exist"""
	message = "User ID not exist"
	def __init__(self):
		super().__init__(message=self.message)


