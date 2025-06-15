from src.core.exceptions.exception import Error

class MessageException(Error):
	message_error = None
	layer = None
	def __init__(self, message: str, layer: str):
		self.message_error = message
		self.layer = layer
	message = f"Domain: Message\nLayer: {layer}\nMessage: {message_error}"