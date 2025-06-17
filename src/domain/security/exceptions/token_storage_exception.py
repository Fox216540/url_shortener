from src.core.exceptions.exception import Error

class TokenStorageException(Error):
	def __init__(self, layer:str, message:str):
		message = f"Security: Token storage\nLayer: {layer}\nMessage: {message}"
		super().__init__(message)