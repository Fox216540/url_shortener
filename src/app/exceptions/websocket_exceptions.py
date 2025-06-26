from src.core.exceptions.exception import Error

LAYER  = "app/service/websocket_service"


class WebsocketException(Error):
	def __init__(self, message:str):
		message = f"App: Websocket_service\nLayer: {LAYER}\nMessage: {message} Error: Server Error"
		super().__init__(message)


class InvalidConnect(WebsocketException):
	"""Invalid Connect"""
	message = "Invalid Connect"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidDisconnect(WebsocketException):
	"""Invalid Disconnect"""
	message = "Invalid Disconnect"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidBroadcast(WebsocketException):
	"""Invalid Broadcast"""
	message = "Invalid Broadcast"
	def __init__(self):
		super().__init__(message=self.message)
