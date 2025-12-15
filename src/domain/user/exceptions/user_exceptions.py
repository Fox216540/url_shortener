from src.core.exceptions.exception import Error

class UserException(Error):
	def __init__(self, layer:str, message:str, error:str):
		message = f"Domain: User\nLayer: {layer}\nMessage: {message}\nError: {error}"
		super().__init__(message)

class UserServerException(UserException):
	def __init__(self, layer:str, message:str):
		super().__init__(layer=layer, message=message, error="Server Error")


class InvalidCreateUser(UserServerException):
	"""Invalid Create User"""
	...


class InvalidExistingUser(UserServerException):
	"""Invalid Existing User"""
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

class UserNotFoundOrAlreadyExistException(UserException):
	def __init__(self, layer:str, message:str):
		super().__init__(layer=layer, message=message, error="Not Found or Already Exist Error")

LAYER = "Domain/User"

class UserNotExists(UserNotFoundOrAlreadyExistException):
	"""User Doesn't exist"""
	...


class InvalidGetUserById(UserNotFoundOrAlreadyExistException):
	"""Invalid Get User By Id"""
	...


class InvalidGetUserByEmail(UserNotFoundOrAlreadyExistException):
	"""Invalid Get User By Email"""
	...


class InvalidGetUserByUsername(UserNotFoundOrAlreadyExistException):
	"""Invalid Get User By Username"""
	...


class InvalidRefreshTokenOfUserType(UserNotFoundOrAlreadyExistException):
	"""Invalid Refresh Token Type"""
	message = "Invalid Refresh Token Type"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InvalidRefreshTokenPayloadOfUserException(UserNotFoundOrAlreadyExistException):
	"""Invalid Refresh Token Payload Exception"""
	message = "Invalid Refresh Token Payload Exception"

	def __init__(self):
		super().__init__(layer=LAYER,message=self.message)

class PasswordIncorrectOfUserException(UserNotFoundOrAlreadyExistException):
	"""Password Incorrect Exception"""
	message = "Password Incorrect Exception"

	def __init__(self):
		super().__init__(layer=LAYER,message=self.message)

class PasswordOfUserAlreadyExistException(UserNotFoundOrAlreadyExistException):
	"""Password Already Exist Exception"""
	message = "Password Already Exist Exception"

	def __init__(self):
		super().__init__(layer=LAYER,message=self.message)

class UsernameOfUserAlreadyExistException(UserNotFoundOrAlreadyExistException):
	"""Username Already Exist Exception"""
	message = "Username Already Exist Exception"

	def __init__(self):
		super().__init__(layer=LAYER,message=self.message)

class NameOfUserAlreadyExistException(UserNotFoundOrAlreadyExistException):
	"""Username Already Exist Exception"""
	message = "Username Already Exist Exception"

	def __init__(self):
		super().__init__(layer=LAYER,message=self.message)

class EmailOfUserAlreadyExistException(UserNotFoundOrAlreadyExistException):
	"""Email Already Exist Exception"""
	message = "Email Already Exist Exception"

	def __init__(self):
		super().__init__(layer=LAYER,message=self.message)