from src.core.exceptions.exception import Error

class MessageException(Error):
	def __init__(self, layer:str, message:str):
		message = f"Domain: Message\nLayer: {layer}\nMessage: {message}"
		super().__init__(message)