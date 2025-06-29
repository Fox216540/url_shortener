from src.core.exceptions.exception import Error

LAYER  = "app/service/health"


class HealthServiceException(Error):
	def __init__(self, message:str):
		message = f"App: Health\nLayer: {LAYER}\nMessage: {message} Error: Server Error"
		super().__init__(message)

class InvalidGetAllHealthStatus(HealthServiceException):
	"""Invalid Get All Health Status"""
	message = "Invalid Get All Health Status"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidGetDbHealthStatus(HealthServiceException):
	"""Invalid Get Db Health Status"""
	message = "Invalid Get Database Health Status"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidGetTsHealthStatus(HealthServiceException):
	"""Invalid Get Ts Health Status"""
	message = "Invalid Get Token Storage Health Status"
	def __init__(self):
		super().__init__(message=self.message)
