from src.core.exceptions.exception import Error

class LinkException(Error):
	def __init__(self, layer:str, message:str):
		message = f"Domain: Link\nLayer: {layer}\nMessage: {message}"
		super().__init__(message)