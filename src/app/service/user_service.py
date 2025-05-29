from typing import Optional
from src.app.service.link_service import LinkService
from src.domain.link.models.link import Link
from src.domain.security.password_hasher import PasswordHasher
from src.domain.security.jwt import JWT
from src.domain.user.models.user import User
from src.app.dtos.auth_dto import AuthResult
from src.domain.user.repositories.user_repo import UserRepository
from uuid import UUID


class UserService:
	def __init__(self, repo: UserRepository, hasher: PasswordHasher, link_service: LinkService, jwt: JWT):
		self.repo = repo
		self.hasher = hasher
		self.link_service = link_service
		self.jwt = jwt

	def register_user(self, email: str, password: str, name: str, username: str) -> Optional[AuthResult]:
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

		auth = AuthResult(
			user=user,
			refresh_token=refresh,
			access_token=access,
		)

		return auth

	def create_user_link(self, user_id: UUID, original_url: str, alias: str = None) -> Optional[Link]:
		return self.link_service.add_link(owner_id=user_id, url=original_url, alias=alias)
