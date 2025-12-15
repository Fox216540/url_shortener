from src.core.exceptions.exception import Error

LAYER  = "Infra/websocket/connection_manager"

class ConnManagerException(Error):
	def __init__(self, message:str):
		message = f"Infra: Websocket\nLayer: {LAYER}\nMessage: {message} Error: Server Error"
		super().__init__(message)


class InvalidConnect(ConnManagerException):
	"""Invalid Connect"""
	message = "Invalid Connect"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidDisconnect(ConnManagerException):
	"""Invalid Disconnect"""
	message = "Invalid Disconnect"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidBroadcast(ConnManagerException):
	"""Invalid Broadcast"""
	message = "Invalid Broadcast"
	def __init__(self):
		super().__init__(message=self.message)

