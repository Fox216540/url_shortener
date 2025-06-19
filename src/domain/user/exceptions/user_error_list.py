from src.domain.user.exceptions.user_exceptions import *

ERRORS_SERVER = [
	InvalidCreateUser,
	InvalidGetUserByUsername,
	InvalidGetUserByEmail,
	InvalidGetUserById,
	UserNotExists,
	InvalidExistingUser,
	InvalidChangeUsername,
	InvalidChangeEmail,
	InvalidChangePassword,
	InvalidChangeName,
	InvalidDelete
]

ERRORS_NOT_FOUND = [
	UserNotExists,
]

ERRORS_USER_REPO = ERRORS_SERVER + ERRORS_NOT_FOUND