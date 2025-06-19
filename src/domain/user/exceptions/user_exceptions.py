from src.core.exceptions.exception import Error

class UserException(Error):
	def __init__(self, layer:str, message:str):
		message = f"Domain: User\nLayer: {layer}\nMessage: {message}"
		super().__init__(message)


class InvalidCreateUser(UserException):
	"""Invalid Create User"""
	...


class UserNotExists(UserException):
	"""User Doesn't exist"""
	...


class InvalidExistingUser(UserException):
	"""Invalid Existing User"""
	...


class InvalidGetUserById(UserException):
	"""Invalid Get User By Id"""
	...


class InvalidGetUserByEmail(UserException):
	"""Invalid Get User By Email"""
	...


class InvalidGetUserByUsername(UserException):
	"""Invalid Get User By Username"""
	...


class InvalidChangePassword(UserException):
	"""Invalid Change Password"""
	...


class InvalidChangeUsername(UserException):
	"""Invalid Change Username"""
	...


class InvalidChangeEmail(UserException):
	"""Invalid Change Email"""
	...


class InvalidChangeName(UserException):
	"""Invalid Change Name"""
	...


class InvalidDelete(UserException):
	"""Invalid Delete"""
	...

