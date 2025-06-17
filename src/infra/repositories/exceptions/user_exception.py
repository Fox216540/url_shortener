from src.domain.user.exceptions.user_exceptions import (
	InvalidCreateUser,
	UserNotExists,
	InvalidExistingUser,
	InvalidGetUserById,
	InvalidGetUserByEmail,
	InvalidGetUserByUsername,
	InvalidChangePassword,
	InvalidChangeUsername,
	InvalidChangeEmail,
	InvalidChangeName,
	InvalidDelete
)

LAYER  = "Infra/repositories/user"


class InfraInvalidCreateUser(InvalidCreateUser):
	"""Invalid Create User"""
	message = "Invalid Create User"
	def __init__(self):
		super().__init__(layer=LAYER , message=self.message)

class InfraUserNotExists(UserNotExists):
	"""User Doesn't exist"""
	message = "User Doesn't Exist"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)
		
class InfraInvalidExistingUser(InvalidExistingUser):
	"""Invalid Existing User"""
	message = "Invalid Existing User"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraInvalidGetUserById(InvalidGetUserById):
	"""Invalid Get User By Id"""
	message = "Invalid Get User By Id"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraInvalidGetUserByEmail(InvalidGetUserByEmail):
	"""Invalid Get User By Email"""
	message = "Invalid Get User By Email"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraInvalidGetUserByUsername(InvalidGetUserByUsername):
	"""Invalid Get User By Username"""
	message = "Invalid Get User By Username"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraInvalidChangePassword(InvalidChangePassword):
	"""Invalid Change Password"""
	message = "Invalid Change Password"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraInvalidChangeUsername(InvalidChangeUsername):
	"""Invalid Change Username"""
	message = "Invalid Change Username"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InfraInvalidChangeEmail(InvalidChangeEmail):
	"""Invalid Change Email"""
	message = "Invalid Change Email"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraInvalidChangeName(InvalidChangeName):
	"""Invalid Change Name"""
	message = "Invalid Change Name"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InfraInvalidDelete(InvalidDelete):
	"""Invalid Delete"""
	message = "Invalid Delete"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)
