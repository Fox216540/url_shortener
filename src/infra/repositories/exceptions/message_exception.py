from src.domain.message.exceptions.message_exceptions import MessageException

LAYER = "Infra/repositories/message"


class InvalidSave(MessageException):
	"""Invalid Save"""
	message = "Invalid User"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InvalidGetMessagesByDate(MessageException):
	"""Invalid Get Messages By Date"""
	message = "Invalid Get Messages By Date"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InvalidDelete(MessageException):
	"""Invalid Delete"""
	message = "Invalid Delete"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InvalidChangeText(MessageException):
	"""Invalid Change Text"""
	message = "Invalid Change Text"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class MessageNotExists(MessageException):
	"""Message Doesn't Exist"""
	message = "Message Doesn't Exist"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class MessagesNotExist(MessageException):
	"""Messages Don't Exist"""
	message = "Messages Don't Exist"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

ERRORS_SERVER = [
	InvalidSave,
	InvalidGetMessagesByDate,
	InvalidDelete,
	InvalidChangeText,
]

ERRORS_NOT_FOUND = [
	MessageNotExists,
]

ERRORS_ALL = ERRORS_SERVER