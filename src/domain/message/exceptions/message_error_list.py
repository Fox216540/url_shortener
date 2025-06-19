from src.domain.message.exceptions.message_exceptions import *

ERRORS_SERVER = [
	InvalidSave,
	InvalidGetMessagesByDate,
	InvalidDelete,
	InvalidChangeText,
]

ERRORS_NOT_FOUND = [
	MessageNotExists,
	MessagesNotExist,
]

ERRORS_MESSAGE_REPO = ERRORS_SERVER + ERRORS_NOT_FOUND