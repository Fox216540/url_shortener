from typing import Optional
from uuid import uuid4
from uuid import UUID
from src.app.service.link_service import LinkService
from src.domain.security.password_hasher import PasswordHasher
from src.app.service.auth_service import AuthService
from src.domain.user.models.user import User
from src.domain.link.models.link import Link
from src.app.dtos.user_dto import UserWithTokens, UserWithAccessToken
from src.domain.user.repositories.user_repo import UserRepository
from src.domain.user.exceptions.user_error_list import ERRORS_USER_REPO as errors_repo
from src.domain.link.exceptions.link_error_list import ERRORS_LINK_REPO as errors_link
from src.domain.security.exceptions.jwt_error_list import ERRORS_JWT as errors_jwt
from src.domain.security.exceptions.token_error_list import ERRORS_TOKEN_STORAGE as errors_token
from src.domain.security.exceptions.password_error_list import ERRORS_PASSWORD_HASHER as errors_hasher


class UserService:
	def __init__(self, repo: UserRepository, hasher: PasswordHasher, link_service: LinkService, auth_service: AuthService):
		self._repo = repo
		self._hasher = hasher
		self._link_service = link_service
		self._auth_service = auth_service

	def register_user(self, email: str, password: str, name: str, username: str) -> Optional[UserWithTokens]:
		try:
			if self._repo.exists_by_email(email):
				raise #TODO: ошибка сервиса
			elif self._repo.exists_by_username(username):
				raise #TODO: ошибка сервиса
			hash_password = self._hasher.hash(password)
			user = User(
				email=email,
				name=name,
				password=hash_password,
				username=username
			)
			saved = self._repo.save(user)

			return self._auth_service.create_tokens_by_user(saved)
		except errors_repo as e:
			raise e
		except errors_hasher as e:
			raise e
		except errors_jwt as e:
			raise e
		except errors_token as e:
			raise e
		except Exception as e:#TODO: ошибка сервиса
			raise e

	def login_user(self, email_or_username: str, password: str) -> Optional[UserWithTokens]:
		try:
			user = self.get_user_by_username(email_or_username) or self._repo.get_by_email(email_or_username)
			self._hasher.verify(password, user.password)
			return self._auth_service.create_tokens_by_user(user)
		except errors_repo as e:
			raise e
		except errors_hasher as e:
			raise e
		except errors_jwt as e:
			raise e
		except errors_token as e:
			raise e
		except Exception as e:#TODO: ошибка сервиса
			raise e

	def create_user_link(self, user_id: UUID, original_url: str, has_room: bool, alias: str = None) -> Optional[Link]:
		try:
			room_id = uuid4() if has_room else None
			link = self._link_service.add_link(owner_id=user_id,
			                                   url=original_url,
			                                   alias=alias,
			                                   room_id=room_id)
			return link
		except errors_link as e:
			raise e
		except Exception as e: #TODO: ошибка сервиса
			raise e

	def change_password(self, user_id: UUID, old_password: str, new_password: str) -> Optional[User]:
		try:
			user = self.get_user_by_id(user_id)

			if not self._hasher.verify(old_password, user.password):
				return None

			if self._hasher.verify(new_password, user.password):
				return None

			hash_password = self._hasher.hash(new_password)
			new_user = self._repo.change_password(user_id, hash_password)

			return new_user
		except errors_hasher as e:
			raise e
		except errors_repo as e:
			raise e
		except Exception as e: #TODO: ошибка сервиса
			raise e

	def change_username(self, user_id: UUID, username: str) -> Optional[UserWithAccessToken]:
		try:
			user = self.get_user_by_id(user_id)

			if user.username == username:
				return None

			if self._repo.exists_by_username(username):
				return None

			new_user = self._repo.change_username(user_id, username)

			return self._auth_service.create_access_token_by_user(new_user)
		except errors_jwt as e:
			raise e
		except errors_repo as e:
			raise e
		except Exception as e: #TODO: ошибка сервиса
			raise e

	def change_name(self, user_id: UUID, name: str) -> Optional[User]:
		try:
			user = self.get_user_by_id(user_id)

			if user.name == name:
				return None

			new_user = self._repo.change_name(user_id, name)

			return new_user
		except errors_repo as e:
			raise e
		except Exception as e: #TODO: ошибка сервиса
			raise e

	def change_email(self, user_id: UUID, email: str) -> Optional[User]:
		try:
			user = self.get_user_by_id(user_id)
			if user.email == email:
				return None

			if self._repo.exists_by_email(email):
				return None

			new_user = self._repo.change_email(user_id, email)

			return new_user
		except errors_repo as e:
			raise e
		except Exception as e: #TODO: ошибка сервиса
			raise e

	def exists_email(self, email: str) -> bool:
		try:
			return self._repo.exists_by_email(email)
		except errors_repo as e:
			raise e
		except Exception as e: #TODO: ошибка сервиса
			raise e

	def exists_username(self, username: str) -> bool:
		try:
			return self._repo.exists_by_username(username)
		except errors_repo as e:
			raise e
		except Exception as e: #TODO: ошибка сервиса
			raise e

	def get_user_by_id(self, user_id: UUID) -> Optional[User]:
		try:
			return self._repo.get_by_id(user_id)
		except errors_repo as e:
			raise e
		except Exception as e: #TODO: ошибка сервиса
			raise e

	def get_user_by_username(self, username: str) -> Optional[User]:
		try:
			return self._repo.get_by_username(username)
		except errors_repo as e:
			raise e
		except Exception as e: #TODO: ошибка сервиса
			raise e

	def _validate_refresh_token(self, token: str) -> tuple[str, UUID] | None:
		try:
			payload = self._auth_service.decode(token)
			if payload.get("type") != "refresh":
				return None

			jti = payload.get("jti")
			sub = payload.get("sub")
			if not jti or not sub:
				return None

			user_id = UUID(sub)
			self._auth_service.exists_refresh(jti)

			return jti, user_id
		except errors_jwt as e:
			raise e
		except errors_token as e:
			raise e
		except Exception as e: #TODO: ошибка сервиса
			raise e

	def refresh_tokens(self, token: str) -> Optional[UserWithTokens]:
		try:
			result = self._validate_refresh_token(token)
			jti, user_id = result

			user = self.get_user_by_id(user_id)

			self._auth_service.delete_refresh(jti, user_id=user.id)

			return self._auth_service.create_tokens_by_user(user)
		except errors_repo as e:
			raise e
		except errors_hasher as e:
			raise e
		except errors_jwt as e:
			raise e
		except errors_token as e:
			raise e
		except Exception as e: #TODO: ошибка сервиса
			raise e

	def logout_user(self, token: str) -> bool | None:
		try:
			result = self._validate_refresh_token(token)
			jti, user_id = result
			return self._auth_service.delete_refresh(jti, user_id)
		except errors_jwt as e:
			raise e
		except errors_token as e:
			raise e
		except Exception as e:  #TODO: ошибка сервиса
			raise e


	def logout_all_user(self, token: str) -> bool | None:
		try:
			result = self._validate_refresh_token(token)
			jti, user_id = result
			return self._auth_service.delete_all_refresh(user_id)
		except errors_jwt as e:
			raise e
		except errors_token as e:
			raise e
		except Exception as e:  #TODO: ошибка сервиса
			raise e

	def delete_link_by_user(self, user_id: UUID, identifier: str) -> Optional[bool]:
		try:
			return self._link_service.delete_link_by_owner_id(identifier, user_id)
		except errors_link as e:
			raise e
		except Exception as e:      #TODO: ошибка сервиса
			raise e

	def delete_all_links_user(self, user_id: UUID) -> Optional[bool]:
		try:
			return self._link_service.delete_all_by_owner_id(user_id)
		except errors_link as e:
			raise e
		except Exception as e:      #TODO: ошибка сервиса
			raise e

	def delete_user(self, user_id: UUID) -> Optional[bool]:
		try:
			self._auth_service.delete_all_refresh(user_id)
			return self._repo.delete(user_id)
		except errors_token as e:
			raise e
		except Exception as e:  #TODO: ошибка сервиса
			raise e
