from src.core.exceptions.exception import Error

class UserException(Error):
	def __init__(self, layer:str, message:str):
		message = f"Domain: User\nLayer: {layer}\nMessage: {message}"
		super().__init__(message)