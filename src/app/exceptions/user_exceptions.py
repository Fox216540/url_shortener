from src.core.exceptions.exception import Error

LAYER  = "app/service/user_service"


class UserException(Error):
	def __init__(self, message:str):
		message = f"App: User_service\nLayer: {LAYER}\nMessage: {message} Error: Server Error"
		super().__init__(message)

class UserServiceException(UserException):
	...

class InvalidRegisterUser(UserServiceException):
	"""Invalid Register User"""
	message = "Invalid Register User"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidLoginUser(UserServiceException):
	"""Invalid Login User"""
	message = "Invalid Login User"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidCreateUserLink(UserServiceException):
	"""Invalid Create User Link"""
	message = "Invalid Create User Link"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidChangePassword(UserServiceException):
	"""Invalid Change Password"""
	message = "Invalid Change Password"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidChangeUsername(UserServiceException):
	"""Invalid Change Username"""
	message = "Invalid Change Username"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidChangeName(UserServiceException):
	"""Invalid Change Name"""
	message = "Invalid Change Name"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidChangeEmail(UserServiceException):
	"""Invalid Change Email"""
	message = "Invalid Change Email"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidExistsEmail(UserServiceException):
	"""Invalid Exists Email"""
	message = "Invalid Exists Email"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidExistsUsername(UserServiceException):
	"""Invalid Exists Username"""
	message = "Invalid Exists Username"
	def __init__(self):
		super().__init__(message=self.message)

class InvalidGetUserById(UserServiceException):
	"""Invalid Get User By Id"""
	message = "Invalid Get User By Id"

	def __init__(self):
		super().__init__(message=self.message)

class InvalidGetUserByUsername(UserServiceException):
	"""Invalid Get User By Username"""
	message = "Invalid Get User By Username"

	def __init__(self):
		super().__init__(message=self.message)

class InvalidRefreshTokens(UserServiceException):
	"""Invalid Refresh Tokens"""
	message = "Invalid Refresh Tokens"

	def __init__(self):
		super().__init__(message=self.message)

class InvalidLogoutUser(UserServiceException):
	"""Invalid Logout User"""
	message = "Invalid Logout User"

	def __init__(self):
		super().__init__(message=self.message)

class InvalidLogoutAllUser(UserServiceException):
	"""Invalid Logout All User"""
	message = "Invalid Logout All User"

	def __init__(self):
		super().__init__(message=self.message)

class InvalidDeleteLinkByUser(UserServiceException):
	"""Invalid Delete Link By User"""
	message = "Invalid Delete Link By User"

	def __init__(self):
		super().__init__(message=self.message)

class InvalidDeleteAllLinksUser(UserServiceException):
	"""Invalid Delete All Links User"""
	message = "Invalid Delete All Links User"

	def __init__(self):
		super().__init__(message=self.message)

class InvalidDeleteUser(UserServiceException):
	"""Invalid Delete User"""
	message = "Invalid Delete User"

	def __init__(self):
		super().__init__(message=self.message)

class UserDataException(UserException):
	...

class InvalidRefreshTokenType(UserDataException):
	"""Invalid Refresh Token Type"""
	message = "Invalid Refresh Token Type"

	def __init__(self):
		super().__init__(message=self.message)

class InvalidRefreshTokenPayloadException(UserDataException):
	"""Invalid Refresh Token Payload Exception"""
	message = "Invalid Refresh Token Payload Exception"

	def __init__(self):
		super().__init__(message=self.message)

class PasswordIncorrectException(UserDataException):
	"""Password Incorrect Exception"""
	message = "Password Incorrect Exception"

	def __init__(self):
		super().__init__(message=self.message)

class PasswordAlreadyExistException(UserDataException):
	"""Password Already Exist Exception"""
	message = "Password Already Exist Exception"

	def __init__(self):
		super().__init__(message=self.message)

class UsernameAlreadyExistException(UserDataException):
	"""Username Already Exist Exception"""
	message = "Username Already Exist Exception"

	def __init__(self):
		super().__init__(message=self.message)

class NameAlreadyExistException(UserDataException):
	"""Username Already Exist Exception"""
	message = "Username Already Exist Exception"

	def __init__(self):
		super().__init__(message=self.message)

class EmailAlreadyExistException(UserDataException):
	"""Email Already Exist Exception"""
	message = "Email Already Exist Exception"

	def __init__(self):
		super().__init__(message=self.message)