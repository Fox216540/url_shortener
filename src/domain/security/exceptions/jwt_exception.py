from src.core.exceptions.exception import Error

class JwtException(Error):
	def __init__(self, layer:str, message:str):
		message = f"Security: Jwt\nLayer: {layer}\nMessage: {message}"
		super().__init__(message)