from src.domain.security.jwt import JWT
from src.domain.user.models.user import User
from src.app.dtos.user_dto import UserResult
from typing import Dict


class AuthService:
	def __init__(self, jwt: JWT):
		self._jwt = jwt

	def refresh_tokens_by_user(self, user: User) -> UserResult:
		refresh = self._jwt.create_refresh_token(user.id)
		access = self._jwt.create_access_token(user.id, user.username)
		return UserResult(user=user, refresh_token=refresh, access_token=access)

	def decode(self, token: str) -> Dict:
		return self._jwt.decode(token)
