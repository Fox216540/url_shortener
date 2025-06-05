from src.domain.security.jwt import JWT
from src.domain.user.models.user import User
from src.domain.security.token_storage import TokenStorage
from src.app.dtos.user_dto import UserWithTokens, UserWithAccessToken
from typing import Dict


class AuthService:
	def __init__(self, jwt: JWT, token_storage: TokenStorage):
		self._jwt = jwt
		self._token_storage = token_storage

	def tokens_by_user(self, user: User) -> UserWithTokens:
		refresh, jti = self._jwt.create_refresh_token(user.id)
		access = self._jwt.create_access_token(user.id, user.username)
		self._token_storage.save_refresh_token(jti)
		return UserWithTokens(refresh_token=refresh, access_token=access, **vars(user))

	def access_token_by_user(self, user: User) -> UserWithAccessToken:
		access = self._jwt.create_access_token(user.id, user.username)
		return UserWithAccessToken(access_token=access, **vars(user))

	def decode(self, token: str) -> Dict:
		return self._jwt.decode(token)

	def delete_refresh(self, jti: str) -> bool:
		return self._token_storage.delete_refresh_token(jti)
