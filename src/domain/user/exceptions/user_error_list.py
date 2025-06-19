from src.domain.user.exceptions.user_exceptions import *

ERRORS_REPO = [
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