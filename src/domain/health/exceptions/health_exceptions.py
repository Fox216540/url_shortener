from src.core.exceptions.exception import Error

class HealthException(Error):
	def __init__(self, layer:str, message:str):
		message = f"Domain: Health\nLayer: {layer}\nMessage: {message}\nError: Server Error"
		super().__init__(message)

class InvalidAllConnection(HealthException):
	"""Invalid All Connection"""
	message = "Invalid All Connection"
	layer = "Domain/health"
	def __init__(self):
		super().__init__(message=self.message, layer=self.layer)

class InvalidTSConnection(HealthException):
	"""Invalid Token Storage Connection"""
	...

class InvalidDbConnection(HealthException):
	"""Invalid DB Connection"""
	...