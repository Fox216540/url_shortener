from src.core.exceptions.exception import Error

class MessageException(Error):
	def __init__(self, layer:str, message:str):
		message = f"Domain: Message\nLayer: {layer}\nMessage: {message}"
		super().__init__(message)


class InvalidSave(MessageException):
	"""Invalid Save"""
	...


class InvalidGetMessagesByDate(MessageException):
	"""Invalid Get Messages By Date"""
	...


class InvalidDelete(MessageException):
	"""Invalid Delete"""
	...


class InvalidChangeText(MessageException):
	"""Invalid Change Text"""
	...

class MessageNotExists(MessageException):
	"""Message Doesn't Exist"""
	...

class MessagesNotExist(MessageException):
	"""Messages Don't Exist"""
	...
