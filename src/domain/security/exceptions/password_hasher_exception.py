from src.core.exceptions.exception import Error

class PasswordHasherException(Error):
	def __init__(self, layer:str, message:str):
		message = f"Security: Password hasher\nLayer: {layer}\nMessage: {message}"
		super().__init__(message)

class InvalidHash(PasswordHasherException):
	"""Invalid Hash"""
	...

class InvalidVerify(PasswordHasherException):
	"""Invalid Verify"""
	...

