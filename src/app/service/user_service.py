from typing import Optional
from src.domain.user.models.user import User
from src.domain.user.repositories.user_repo import UserRepository
from src.app.service.link_service import LinkService
from src.domain.link.models.link import Link
from src.domain.security.password_hasher import PasswordHasher

from uuid import UUID


class UserService:
	def __init__(self, repo: UserRepository, hasher: PasswordHasher, link_service: LinkService):
		self.repo = repo
		self.hasher = hasher
		self.link_service = link_service

	def register_user(self, email: str, password: str, name: str, username: str) -> Optional[User]:
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
		return saved

	def authenticate(self, email: str, password: str) -> Optional[User]:
		"""Аутентификация пользователя"""
		user = self.repo.get_by_email(email)  # Используем новый метод
		if not user:
			return None

		if not self.hasher.verify(password, user.password):
			return None

		return user

	def create_user_link(self, email: str, password: str, original_url: str, alias: str = None) -> Optional[Link]:
		user = self.authenticate(email=email, password=password)
		return self.link_service.add_link(owner_id=user.id, url=original_url, alias=alias)
