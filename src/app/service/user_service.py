from typing import Optional
from src.app.service.link_service import LinkService
from src.domain.link.models.link import Link
from src.domain.security.password_hasher import PasswordHasher
from src.domain.security.jwt import JWT
from src.domain.user.models.user import User
from src.app.dtos.user_dto import UserResult
from src.domain.user.repositories.user_repo import UserRepository
from uuid import UUID


class UserService:
	def __init__(self, repo: UserRepository, hasher: PasswordHasher, link_service: LinkService, jwt: JWT):
		self.repo = repo
		self.hasher = hasher
		self.link_service = link_service
		self.jwt = jwt

	def register_user(self, email: str, password: str, name: str, username: str) -> Optional[UserResult]:
		if self.repo.exists_by_email(email):
			return None
		elif self.repo.exists_by_username(username):
			return None
		hash_password = self.hasher.hash(password)
		user = User(
			email=email,
			name=name,
			password=hash_password,
			username=username
		)
		saved = self.repo.save(user)
		if not saved:
			pass

		refresh = self.jwt.create_refresh_token(saved.id)
		access = self.jwt.create_access_token(saved.id, saved.username)

		auth = UserResult(
			user=user,
			refresh_token=refresh,
			access_token=access,
		)

		return auth

	def create_user_link(self, user_id: UUID, original_url: str, alias: str = None) -> Optional[Link]:
		return self.link_service.add_link(owner_id=user_id, url=original_url, alias=alias)

	def change_password(self, user_id: UUID, old_password: str, new_password: str) -> Optional[UserResult]:
		user = self.repo.get_by_id(user_id)

		if not self.hasher.verify(old_password, user.password):
			return None

		if self.hasher.verify(new_password, user.password):
			return None

		hash_password = self.hasher.hash(new_password)
		new_user = self.repo.change_password(user_id, hash_password)

		refresh = self.jwt.create_refresh_token(new_user.id)
		access = self.jwt.create_access_token(new_user.id, new_user.username)

		auth = UserResult(
			user=new_user,
			refresh_token=refresh,
			access_token=access,
		)

		return auth

	def change_username(self, user_id: UUID, username: str) -> Optional[UserResult]:
		user = self.repo.get_by_id(user_id)

		if user.username == username:
			return None

		if self.repo.exists_by_username(username):
			return None

		new_user = self.repo.change_username(user_id, username)
		refresh = self.jwt.create_refresh_token(new_user.id)
		access = self.jwt.create_access_token(new_user.id, new_user.username)

		auth = UserResult(
			user=new_user,
			refresh_token=refresh,
			access_token=access,
		)

		return auth

	def change_name(self, user_id: UUID, name: str) -> Optional[UserResult]:
		user = self.repo.get_by_id(user_id)

		if user.name == name:
			return None

		new_user = self.repo.change_name(user_id, name)
		refresh = self.jwt.create_refresh_token(new_user.id)
		access = self.jwt.create_access_token(new_user.id, new_user.username)

		auth = UserResult(
			user=new_user,
			refresh_token=refresh,
			access_token=access,
		)

		return auth

	def change_email(self, user_id: UUID, email: str) -> Optional[UserResult]:
		user = self.repo.get_by_id(user_id)

		if user.email == email:
			return None

		if self.repo.exists_by_email(email):
			return None

		new_user = self.repo.change_email(user_id, email)
		refresh = self.jwt.create_refresh_token(new_user.id)
		access = self.jwt.create_access_token(new_user.id, new_user.username)

		auth = UserResult(
			user=new_user,
			refresh_token=refresh,
			access_token=access,
		)

		return auth
