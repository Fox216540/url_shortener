from src.core.exceptions.exception import Error

class UserException(Error):
	def __init__(self, layer:str, message:str, error:str):
		message = f"Domain: User\nLayer: {layer}\nMessage: {message}\nError: {error}"
		super().__init__(message)

class UserServerException(UserException):
	def __init__(self, layer:str, message:str):
		super().__init__(layer=layer, message=message, error="Server Error")

class UserNotFoundException(UserException):
	def __init__(self, layer:str, message:str):
		super().__init__(layer=layer, message=message, error="Not Found Error")



class InvalidCreateUser(UserServerException):
	"""Invalid Create User"""
	...


class UserNotExists(UserNotFoundException):
	"""User Doesn't exist"""
	...


class InvalidExistingUser(UserServerException):
	"""Invalid Existing User"""
	...


class InvalidGetUserById(UserServerException):
	"""Invalid Get User By Id"""
	...


class InvalidGetUserByEmail(UserServerException):
	"""Invalid Get User By Email"""
	...


class InvalidGetUserByUsername(UserServerException):
	"""Invalid Get User By Username"""
	...


class InvalidChangePassword(UserServerException):
	"""Invalid Change Password"""
	...


class InvalidChangeUsername(UserServerException):
	"""Invalid Change Username"""
	...


class InvalidChangeEmail(UserServerException):
	"""Invalid Change Email"""
	...


class InvalidChangeName(UserServerException):
	"""Invalid Change Name"""
	...


class InvalidDelete(UserServerException):
	"""Invalid Delete"""
	...

