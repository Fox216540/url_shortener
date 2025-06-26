from src.core.exceptions.exception import Error

LAYER  = "app/service/user_exceptions"


class UserException(Error):
	def __init__(self, message:str):
		message = f"App: Auth_service\nLayer: {LAYER}\nMessage: {message} Error: Server Error"
		super().__init__(message)


class InvalidRegisterUser(UserException):
	"""Invalid Register User"""
	message = "Invalid Register User"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidLoginUser(UserException):
	"""Invalid Login User"""
	message = "Invalid Login User"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidCreateUserLink(UserException):
	"""Invalid Create User Link"""
	message = "Invalid Create User Link"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidChangePassword(UserException):
	"""Invalid Change Password"""
	message = "Invalid Change Password"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidChangeUsername(UserException):
	"""Invalid Change Username"""
	message = "Invalid Change Username"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidChangeName(UserException):
	"""Invalid Change Name"""
	message = "Invalid Change Name"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidChangeEmail(UserException):
	"""Invalid Change Email"""
	message = "Invalid Change Email"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidExistsEmail(UserException):
	"""Invalid Exists Email"""
	message = "Invalid Exists Email"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidExistsUsername(UserException):
	"""Invalid Exists Username"""
	message = "Invalid Exists Username"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidGetUserById(UserException):
	"""Invalid Get User By Id"""
	message = "Invalid Get User By Id"

	def __init__(self):
		super().__init__(message=self.message)

class InvalidGetUserByUsername(UserException):
	"""Invalid Get User By Username"""
	message = "Invalid Get User By Username"

	def __init__(self):
		super().__init__(message=self.message)

class InvalidRefreshTokens(UserException):
	"""Invalid Refresh Tokens"""
	message = "Invalid Refresh Tokens"

	def __init__(self):
		super().__init__(message=self.message)

class InvalidLogoutUser(UserException):
	"""Invalid Logout User"""
	message = "Invalid Logout User"

	def __init__(self):
		super().__init__(message=self.message)

class InvalidLogoutAllUser(UserException):
	"""Invalid Logout All User"""
	message = "Invalid Logout All User"

	def __init__(self):
		super().__init__(message=self.message)

class InvalidDeleteLinkByUser(UserException):
	"""Invalid Delete Link By User"""
	message = "Invalid Delete Link By User"

	def __init__(self):
		super().__init__(message=self.message)

class InvalidDeleteAllLinksUser(UserException):
	"""Invalid Delete All Links User"""
	message = "Invalid Delete All Links User"

	def __init__(self):
		super().__init__(message=self.message)

class InvalidDeleteUser(UserException):
	"""Invalid Delete User"""
	message = "Invalid Delete User"

	def __init__(self):
		super().__init__(message=self.message)