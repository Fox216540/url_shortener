from src.domain.message.exceptions.message_exceptions import (
	InvalidSave,
	InvalidGetMessagesByDate,
	InvalidDelete,
	InvalidChangeText,
	MessageNotExists,
	MessagesNotExist
)

LAYER = "Infra/repositories/message"


class InfraInvalidSave(InvalidSave):
	message = "Invalid User"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InfraInvalidGetMessagesByDate(InvalidGetMessagesByDate):
	message = "Invalid Get Messages By Date"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InfraInvalidDelete(InvalidDelete):
	message = "Invalid Delete"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InfraInvalidChangeText(InvalidChangeText):
	message = "Invalid Change Text"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraMessageNotExists(MessageNotExists):
	message = "Message Doesn't Exist"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraMessagesNotExist(MessagesNotExist):
	message = "Messages Don't Exist"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)
