from src.core.exceptions.exception import Error

LAYER  = "Infra/websocket/connection_manager"

def get_message(message: str) -> str:
	return f"Infra: Websocket\nLayer: {LAYER}\nMessage: {message}"

class InvalidConnect(Error):
	"""Invalid Connect"""
	message = "Invalid Connect"
	def __init__(self):
		super().__init__(get_message(message=self.message))

class InvalidDisconnect(Error):
	"""Invalid Disconnect"""
	message = "Invalid Disconnect"
	def __init__(self):
		super().__init__(get_message(message=self.message))

class InvalidBroadcast(Error):
	"""Invalid Broadcast"""
	message = "Invalid Broadcast"
	def __init__(self):
		super().__init__(get_message(message=self.message))


ERRORS_SERVER = [
	InvalidConnect,
	InvalidBroadcast,
	InvalidDisconnect,
]

ERRORS_ALL = ERRORS_SERVER
