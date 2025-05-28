from typing import Optional
from src.domain.user.models.user import User
from src.domain.user.repositories.user_repo import UserRepository

from src.app.service.success import success_message_create_user

from src.domain.security.password_hasher import PasswordHasher


class UserService:
	def __init__(self, repo: UserRepository, hasher: PasswordHasher):
		self.repo = repo
		self.hasher = hasher

	def create_user(self, user: User) -> Optional[str]:
		user.password = self.hasher.hash(user.password)
		saved = self.repo.create(user)
		if saved:
			return success_message_create_user

	def get_id_by_mail_password(self, mail: str, password: str) -> Optional[User]:
		user = self.repo.get_by_mail(mail=mail)  # запрашиваем по почте и паролю
		if not user:
			return None
		if not self.hasher.verify(password, user.password):
			return None
		return user.id
