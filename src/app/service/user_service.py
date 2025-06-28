from uuid import uuid4
from uuid import UUID
from pydantic import HttpUrl, EmailStr, TypeAdapter
from src.app.service.link_service import LinkService
from src.domain.security.password_hasher import PasswordHasher
from src.app.service.auth_service import AuthService
from src.domain.user.models.user import User
from src.domain.link.models.link import Link
from src.app.dtos.user_dto import UserWithTokens, UserWithAccessToken
from src.domain.user.repositories.user_repo import UserRepository
from src.domain.user.exceptions.user_exceptions import UserException, UserNotFoundException
from src.domain.link.exceptions.link_exceptions import LinkException
from src.domain.security.exceptions.jwt_exception import JwtException
from src.domain.security.exceptions.token_storage_exception import TokenStorageException
from src.domain.security.exceptions.password_hasher_exception import PasswordHasherException
from src.app.exceptions.user_exceptions import (
	UserServiceException, UserDataException,
	InvalidRegisterUser, InvalidGetUserByUsername, InvalidDeleteUser,
	InvalidChangePassword,InvalidChangeUsername, InvalidChangeName,
	InvalidChangeEmail, InvalidExistsEmail,InvalidExistsUsername,
	InvalidCreateUserLink, InvalidLoginUser, InvalidRefreshTokens,
	InvalidLogoutUser, InvalidLogoutAllUser, InvalidDeleteLinkByUser,
	InvalidDeleteAllLinksUser, InvalidGetUserById, InvalidRefreshTokenPayloadException,
	InvalidRefreshTokenType, PasswordIncorrectException, PasswordAlreadyExistException,
	UsernameAlreadyExistException, NameAlreadyExistException, EmailAlreadyExistException,
)
from src.logger import error_logger


class UserService:
	def __init__(self, repo: UserRepository, hasher: PasswordHasher, link_service: LinkService,
	             auth_service: AuthService):
		self._repo = repo
		self._hasher = hasher
		self._link_service = link_service
		self._auth_service = auth_service

	def register_user(self, email: EmailStr, password: str, name: str, username: str) -> UserWithTokens:
		try:
			if self._repo.exists_by_email(email):
				raise InvalidRegisterUser()
			elif self._repo.exists_by_username(username):
				raise InvalidRegisterUser()
			hash_password = self._hasher.hash(password)
			user = User(
				email=email,
				name=name,
				password=hash_password,
				username=username
			)
			saved = self._repo.save(user)

			return self._auth_service.create_tokens_by_user(saved)
		except (InvalidRegisterUser, UserException, PasswordHasherException, JwtException, TokenStorageException) as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidRegisterUser() from e

	def login_user(self, email_or_username: str, password: str) -> UserWithTokens:
		try:
			try:
				user = self.get_user_by_username(email_or_username)
			except UserNotFoundException:
				email_adapter = TypeAdapter(EmailStr)
				email = email_adapter.validate_python(email_or_username)
				user = self.get_user_by_email(email)
			if not self._hasher.verify(password, user.password):
				raise PasswordIncorrectException()
			return self._auth_service.create_tokens_by_user(user)
		except (
				UserServiceException, UserDataException,
				UserException, PasswordHasherException,
				JwtException, TokenStorageException
		) as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidLoginUser() from e

	def create_user_link(self, user_id: UUID, original_url: HttpUrl, has_room: bool = None, alias: str = None) -> Link:
		try:
			room_id = uuid4() if has_room else None
			link = self._link_service.add_link(owner_id=user_id,
			                                   url=original_url,
			                                   alias=alias,
			                                   room_id=room_id)
			return link
		except LinkException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidCreateUserLink() from e

	def change_password(self, user_id: UUID, old_password: str, new_password: str) -> User:
		try:
			user = self.get_user_by_id(user_id)

			if not self._hasher.verify(old_password, user.password):
				raise PasswordIncorrectException()

			if self._hasher.verify(new_password, user.password):
				raise PasswordAlreadyExistException()

			hash_password = self._hasher.hash(new_password)
			new_user = self._repo.change_password(user_id, hash_password)

			return new_user
		except (
				UserException, UserServiceException,
				UserDataException, PasswordHasherException,
				InvalidChangePassword
		) as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidChangePassword() from e

	def change_username(self, user_id: UUID, username: str) -> UserWithAccessToken:
		try:
			user = self.get_user_by_id(user_id)

			if user.username == username or self._repo.exists_by_username(username):
				raise UsernameAlreadyExistException()

			new_user = self._repo.change_username(user_id, username)

			return self._auth_service.create_access_token_by_user(new_user)
		except (
				UserServiceException, UserDataException,
				JwtException, UserException,
				InvalidChangeUsername
		) as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidChangeUsername() from e

	def change_name(self, user_id: UUID, name: str) -> User:
		try:
			user = self.get_user_by_id(user_id)

			if user.name == name:
				raise NameAlreadyExistException()

			new_user = self._repo.change_name(user_id, name)

			return new_user
		except (
				UserServiceException, UserDataException,
				UserException, InvalidChangeName
		) as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidChangeName() from e

	def change_email(self, user_id: UUID, email: EmailStr) -> User:
		try:
			user = self.get_user_by_id(user_id)
			if user.email == email or not self._repo.exists_by_email(email):
				raise EmailAlreadyExistException()

			new_user = self._repo.change_email(user_id, email)

			return new_user
		except (
				UserServiceException, UserDataException,
				UserException, InvalidChangeEmail
		) as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidChangeEmail() from e

	def exists_email(self, email: EmailStr) -> bool:
		try:
			return self._repo.exists_by_email(email)
		except UserException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidExistsEmail() from e

	def exists_username(self, username: str) -> bool:
		try:
			return self._repo.exists_by_username(username)
		except UserException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidExistsUsername() from e

	def get_user_by_id(self, user_id: UUID) -> User:
		try:
			return self._repo.get_by_id(user_id)
		except UserException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidGetUserById() from e

	def get_user_by_username(self, username: str) -> User:
		try:
			return self._repo.get_by_username(username)
		except UserException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidGetUserByUsername() from e

	def get_user_by_email(self, email: EmailStr) -> User:
		try:
			return self._repo.get_by_email(email)
		except UserException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidGetUserById() from e

	def _validate_refresh_token(self, token: str) -> tuple[str, UUID]:
		try:
			payload = self._auth_service.decode(token)
			if payload.get("type") != "refresh":
				raise InvalidRefreshTokenType()

			jti = payload.get("jti")
			sub = payload.get("sub")
			if not jti or not sub:
				raise InvalidRefreshTokenPayloadException()

			user_id = UUID(sub)
			self._auth_service.exists_refresh(jti)

			return jti, user_id
		except Exception as e:
			raise e

	def refresh_tokens(self, token: str) -> UserWithTokens:
		try:
			result = self._validate_refresh_token(token)
			jti, user_id = result

			user = self.get_user_by_id(user_id)

			self._auth_service.delete_refresh(jti, user_id=user.id)

			return self._auth_service.create_tokens_by_user(user)
		except (
				UserServiceException, UserDataException,
				UserException, JwtException,
				PasswordHasherException, TokenStorageException
		) as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidRefreshTokens() from e

	def logout_user(self, token: str) -> bool:
		try:
			result = self._validate_refresh_token(token)
			jti, user_id = result
			return self._auth_service.delete_refresh(jti, user_id)
		except (UserDataException, JwtException, TokenStorageException) as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidLogoutUser() from e

	def logout_all_user(self, token: str) -> bool:
		try:
			result = self._validate_refresh_token(token)
			jti, user_id = result
			return self._auth_service.delete_all_refresh(user_id)
		except (UserDataException, JwtException, TokenStorageException) as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidLogoutAllUser() from e

	def delete_link_by_user(self, user_id: UUID, identifier: str) -> bool:
		try:
			return self._link_service.delete_link_by_owner_id(identifier, user_id)
		except LinkException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidDeleteLinkByUser() from e

	def delete_all_links_user(self, user_id: UUID) -> bool:
		try:
			return self._link_service.delete_all_by_owner_id(user_id)
		except LinkException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidDeleteAllLinksUser() from e

	def delete_user(self, user_id: UUID) -> bool:
		try:
			self._auth_service.delete_all_refresh(user_id)
			return self._repo.delete(user_id)
		except TokenStorageException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidDeleteUser() from e
