from src.domain.security.jwt import JWT
from src.domain.user.models.user import User
from src.app.dtos.user_dto import UserWithTokens, UserWithAccessToken
from typing import Dict


class AuthService:
	def __init__(self, jwt: JWT):
		self._jwt = jwt

	def tokens_by_user(self, user: User) -> UserWithTokens:
		refresh = self._jwt.create_refresh_token(user.id)
		access = self._jwt.create_access_token(user.id, user.username)
		return UserWithTokens(refresh_token=refresh, access_token=access, **vars(user))

	def access_token_by_user(self, user: User) -> UserWithAccessToken:
		access = self._jwt.create_access_token(user.id, user.username)
		return UserWithAccessToken(access_token=access, **vars(user))

	def decode(self, token: str) -> Dict:
		return self._jwt.decode(token)
