from src.core.exceptions.exception import Error

LAYER  = "api/health_handler"


class HealthHandlerException(Error):
	def __init__(self, message:str):
		message = f"Api: Health_handler\nLayer: {LAYER}\nMessage: {message} Error: Not Found"
		super().__init__(message)


class NameOfHealthNotExist(HealthHandlerException):
	"""Name of Health not exist"""
	message = "Name of Health not exist"
	def __init__(self):
		super().__init__(message=self.message)


