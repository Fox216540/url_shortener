from typing import Optional
from src.app.service.link_service import LinkService
from src.domain.security.password_hasher import PasswordHasher
from src.domain.security.jwt import JWT
from src.domain.user.models.user import User
from src.app.dtos.user_dto import UserResult, UserResultWithLink
from src.domain.user.repositories.user_repo import UserRepository
from uuid import UUID


class UserService:
	def __init__(self, repo: UserRepository, hasher: PasswordHasher, link_service: LinkService, jwt: JWT):
		self._repo = repo
		self._hasher = hasher
		self._link_service = link_service
		self._jwt = jwt

	def _build_auth_response(self, user: User) -> UserResult:
		refresh = self._jwt.create_refresh_token(user.id)
		access = self._jwt.create_access_token(user.id, user.username)
		return UserResult(user=user, refresh_token=refresh, access_token=access)

	def register_user(self, email: str, password: str, name: str, username: str) -> Optional[UserResult]:
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

		return self._build_auth_response(saved)

	def create_user_link(self, user_id: UUID, original_url: str, alias: str = None) -> Optional[UserResultWithLink]:
		user_data = self._build_auth_response(self._repo.get_by_id(user_id))
		link = self._link_service.add_link(owner_id=user_id, url=original_url, alias=alias)

		return UserResultWithLink(
			user=user_data.user,
			access_token=user_data.access_token,
			refresh_token=user_data.refresh_token,
			link=link
		)

	def change_password(self, user_id: UUID, old_password: str, new_password: str) -> Optional[UserResult]:
		user = self._repo.get_by_id(user_id)

		if not self._hasher.verify(old_password, user.password):
			return None

		if self._hasher.verify(new_password, user.password):
			return None

		hash_password = self._hasher.hash(new_password)
		new_user = self._repo.change_password(user_id, hash_password)

		return self._build_auth_response(new_user)

	def change_username(self, user_id: UUID, username: str) -> Optional[UserResult]:
		user = self._repo.get_by_id(user_id)

		if user.username == username:
			return None

		if self._repo.exists_by_username(username):
			return None

		new_user = self._repo.change_username(user_id, username)

		return self._build_auth_response(new_user)

	def change_name(self, user_id: UUID, name: str) -> Optional[UserResult]:
		user = self._repo.get_by_id(user_id)

		if user.name == name:
			return None

		new_user = self._repo.change_name(user_id, name)

		return self._build_auth_response(new_user)

	def change_email(self, user_id: UUID, email: str) -> Optional[UserResult]:
		user = self._repo.get_by_id(user_id)

		if user.email == email:
			return None

		if self._repo.exists_by_email(email):
			return None

		new_user = self._repo.change_email(user_id, email)

		return self._build_auth_response(new_user)

	def exist_email(self, email: str):
		pass

	def exist_username(self, username: str):
		pass
