from src.core.exceptions.exception import Error

class HealthException(Error):
	def __init__(self, layer:str, message:str, error:str):
		message = f"Domain: Health\nLayer: {layer}\nMessage: {message}\nError: {error}"
		super().__init__(message)

LAYER  = "Domain/health"

class HealthServerException(HealthException):
	def __init__(self, layer:str, message:str):
		super().__init__(layer=layer, message=message, error="Server Error")


class InvalidAllConnection(HealthServerException):
	"""Invalid All Connection"""
	message = "Invalid All Connection"
	def __init__(self):
		super().__init__(message=self.message, layer=LAYER)

class InvalidTSConnection(HealthServerException):
	"""Invalid Token Storage Connection"""
	...

class InvalidDbConnection(HealthServerException):
	"""Invalid DB Connection"""
	...

class HealthNotFoundException(HealthException):
	def __init__(self, layer: str, message: str):
		super().__init__(layer=layer, message=message, error="Not Found Error")

class NameOfHealthNotExist(HealthNotFoundException):
	"""Name of Health not exist"""
	message = "Name of Health not exist"
	def __init__(self):
		super().__init__(message=self.message,layer=LAYER)