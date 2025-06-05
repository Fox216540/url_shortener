from typing import Optional
from src.app.service.link_service import LinkService
from src.domain.security.password_hasher import PasswordHasher
from src.app.service.auth_service import AuthService
from src.domain.user.models.user import User
from src.domain.link.models.link import Link
from src.app.dtos.user_dto import UserWithTokens,UserWithAccessToken
from src.domain.user.repositories.user_repo import UserRepository
from src.logger import status_logger
from uuid import UUID


class UserService:
	def __init__(self, repo: UserRepository, hasher: PasswordHasher, link_service: LinkService, auth_service: AuthService):
		self._repo = repo
		self._hasher = hasher
		self._link_service = link_service
		self._auth_service = auth_service

	def register_user(self, email: str, password: str, name: str, username: str) -> Optional[UserWithTokens]:
		if self._repo.exists_by_email(email):
			return None
		elif self._repo.exists_by_username(username):
			return None
		hash_password = self._hasher.hash(password)
		user = User(
			email=email,
			name=name,
			password=hash_password,
			username=username
		)
		saved = self._repo.save(user)
		if not saved:
			pass

		return self._auth_service.tokens_by_user(saved)

	def login_user(self, email_or_username: str, password: str) -> Optional[UserWithTokens]:
		user = self.get_user_by_username(email_or_username) or self._repo.get_by_email(email_or_username)

		if not user:
			return None

		if not self._hasher.verify(password, user.password):
			return None

		return self._auth_service.tokens_by_user(user)

	def create_user_link(self, user_id: UUID, original_url: str, alias: str = None) -> Optional[Link]:
		link = self._link_service.add_link(owner_id=user_id, url=original_url, alias=alias)
		return link

	def change_password(self, user_id: UUID, old_password: str, new_password: str) -> Optional[User]:
		user = self.get_user_by_id(user_id)

		if not self._hasher.verify(old_password, user.password):
			return None

		if self._hasher.verify(new_password, user.password):
			return None

		hash_password = self._hasher.hash(new_password)
		new_user = self._repo.change_password(user_id, hash_password)

		return new_user

	def change_username(self, user_id: UUID, username: str) -> Optional[UserWithAccessToken]:
		user = self.get_user_by_id(user_id)

		if user.username == username:
			return None

		if self._repo.exists_by_username(username):
			return None

		new_user = self._repo.change_username(user_id, username)

		return self._auth_service.access_token_by_user(new_user)

	def change_name(self, user_id: UUID, name: str) -> Optional[User]:
		user = self.get_user_by_id(user_id)

		if user.name == name:
			return None

		new_user = self._repo.change_name(user_id, name)

		return new_user

	def change_email(self, user_id: UUID, email: str) -> Optional[User]:
		user = self.get_user_by_id(user_id)

		if user.email == email:
			return None

		if self._repo.exists_by_email(email):
			return None

		new_user = self._repo.change_email(user_id, email)

		return new_user

	def exists_email(self, email: str) -> bool:
		return self._repo.exists_by_email(email)

	def exists_username(self, username: str) -> bool:
		return self._repo.exists_by_username(username)

	def get_user_by_id(self, user_id: UUID) -> Optional[User]:
		return self._repo.get_by_id(user_id)

	def get_user_by_username(self, username: str) -> Optional[User]:
		return self._repo.get_by_username(username)

	def refresh_tokens(self, token: str) -> Optional[UserWithTokens]:
		payload = self._auth_service.decode(token)
		if payload.get("type") != "refresh":
			return None

		jti = payload.get("jti")
		if not jti or not self._auth_service.exists_refresh(jti):
			return None

		user = self.get_user_by_id(UUID(payload["sub"]))
		if not user:
			return None

		self._auth_service.delete_refresh(payload.get("jti"))
		return self._auth_service.tokens_by_user(user)

	def logout_user(self, token: str) -> bool | None:
		payload = self._auth_service.decode(token)
		if payload.get("type") != "refresh":
			return None

		jti = payload.get("jti")
		if not jti or not self._auth_service.exists_refresh(jti):
			return None

		return self._auth_service.delete_refresh(jti)

	def delete_link_by_user(self, user_id: UUID, identifier: str) -> Optional[bool]:
		return self._link_service.delete_link_by_owner_id(identifier, user_id)

	def delete_all_user(self, user_id: UUID) -> Optional[bool]:
		return self._link_service.delete_all_by_owner_id(user_id)
