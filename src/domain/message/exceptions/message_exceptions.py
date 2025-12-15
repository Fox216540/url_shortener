from src.core.exceptions.exception import Error

class MessageException(Error):
	def __init__(self, layer:str, message:str, error:str):
		message = f"Domain: Message\nLayer: {layer}\nMessage: {message}\nError: {error}"
		super().__init__(message)


class MessageServerException(MessageException):
	def __init__(self, layer:str, message:str):
		super().__init__(layer=layer, message=message, error="Server Error")

class InvalidSave(MessageServerException):
	"""Invalid Save"""
	...


class InvalidGetMessagesByDate(MessageServerException):
	"""Invalid Get Messages By Date"""
	...


class InvalidDelete(MessageServerException):
	"""Invalid Delete"""
	...


class InvalidChangeText(MessageServerException):
	"""Invalid Change Text"""
	...

class MessageNotFoundException(MessageException):
	def __init__(self, layer:str, message:str):
		super().__init__(layer=layer, message=message, error="Not Found Error")

class MessageNotExists(MessageNotFoundException):
	"""Message Doesn't Exist"""
	...

class MessagesNotExist(MessageNotFoundException):
	"""Messages Don't Exist"""
	...

class UserIdOfMessageNotExist(MessageNotFoundException):
	"""User ID of message not exist"""
	message = "User ID not exist"
	layer = "Domain/Message"
	def __init__(self):
		super().__init__(layer=self.layer, message=self.message)