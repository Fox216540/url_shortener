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
	message = "Invalid Create User"
	def __init__(self):
		super().__init__(layer=LAYER , message=self.message)

class InfraUserNotExists(UserNotExists):
	message = "User Doesn't Exist"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)
		
class InfraInvalidExistingUser(InvalidExistingUser):
	message = "Invalid Existing User"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraInvalidGetUserById(InvalidGetUserById):
	message = "Invalid Get User By Id"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraInvalidGetUserByEmail(InvalidGetUserByEmail):
	message = "Invalid Get User By Email"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraInvalidGetUserByUsername(InvalidGetUserByUsername):
	message = "Invalid Get User By Username"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraInvalidChangePassword(InvalidChangePassword):
	message = "Invalid Change Password"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraInvalidChangeUsername(InvalidChangeUsername):
	message = "Invalid Change Username"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InfraInvalidChangeEmail(InvalidChangeEmail):
	message = "Invalid Change Email"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraInvalidChangeName(InvalidChangeName):
	message = "Invalid Change Name"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InfraInvalidDelete(InvalidDelete):
	message = "Invalid Delete"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)
