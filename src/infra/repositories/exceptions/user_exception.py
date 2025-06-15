from src.domain.user.exceptions.user_exceptions import UserException

LAYER  = "Infra/repositories"


class InvalidCreateUser(UserException):
	"""Invalid User"""
	message = "Invalid User"
	def __init__(self):
		super().__init__(layer=LAYER , message=self.message)

class UserNotExists(UserException):
	"""User not exists"""
	message = "User not found"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InvalidGetUserById(UserException):
	"""Invalid Get User By Id"""
	message = "Invalid Get User By Id"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InvalidGetUserByEmail(UserException):
	"""Invalid Get User By Email"""
	message = "Invalid Get User By Email"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InvalidGetUserByUsername(UserException):
	"""Invalid Get User By Username"""
	message = "Invalid Get User By Username"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InvalidChangePassword(UserException):
	"""Invalid Change Password"""
	message = "Invalid Change Password"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InvalidChangeUsername(UserException):
	"""Invalid Change Username"""
	message = "Invalid Change Username"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InvalidChangeEmail(UserException):
	"""Invalid Change Email"""
	message = "Invalid Change Email"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InvalidChangeName(UserException):
	"""Invalid Change Name"""
	message = "Invalid Change Name"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InvalidDelete(UserException):
	"""Invalid Delete"""
	message = "Invalid Delete"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


ERRORS_SERVER = [
	InvalidCreateUser,
	InvalidGetUserById,
	InvalidGetUserByEmail,
	InvalidGetUserByUsername,
	InvalidChangePassword,
	InvalidChangeUsername,
	InvalidChangeEmail,
	InvalidChangeName,
	InvalidDelete,
]

ERRORS_NOT_FOUND = [
	UserNotExists
]

ERRORS_ALL = ERRORS_SERVER + ERRORS_NOT_FOUND