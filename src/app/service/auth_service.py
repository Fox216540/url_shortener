from uuid import UUID
from typing import Dict
from src.domain.security.jwt import JWT
from src.domain.user.models.user import User
from src.domain.security.token_storage import TokenStorage
from src.app.dtos.user_dto import UserWithTokens, UserWithAccessToken
from src.domain.security.exceptions.jwt_exception import JwtException
from src.domain.security.exceptions.token_storage_exception import TokenStorageException
from src.app.exceptions.auth_exceptions import (
	InvalidCreateAccessToken,
	InvalidDecode,
	InvalidCreateTokens,
	InvalidDeleteRefresh,
	InvalidDeleteAllRefresh,
	InvalidExistsRefresh
)



class AuthService:
	def __init__(self, jwt: JWT, token_storage: TokenStorage):
		self._jwt = jwt
		self._token_storage = token_storage

	def create_tokens_by_user(self, user: User) -> UserWithTokens:
		try:
			refresh, jti = self._jwt.create_refresh_token(user.id)
			access = self._jwt.create_access_token(user.id, user.username)
			self._token_storage.save_refresh_token(jti=jti, user_id=user.id)
			return UserWithTokens(refresh_token=refresh, access_token=access, **vars(user))
		except (JwtException, TokenStorageException) as e:
			raise e
		except Exception as e:
			raise InvalidCreateTokens() from e

	def create_access_token_by_user(self, user: User) -> UserWithAccessToken:
		try:
			access = self._jwt.create_access_token(user.id, user.username)
			return UserWithAccessToken(access_token=access, **vars(user))
		except JwtException as e:
			raise e
		except Exception as e:
			raise InvalidCreateAccessToken() from e

	def decode(self, token: str) -> Dict:
		try:
			return self._jwt.decode(token)
		except JwtException as e:
			raise e
		except Exception as e:
			raise InvalidDecode() from e

	def delete_refresh(self, jti: str, user_id: UUID) -> bool:
		try:
			return self._token_storage.delete_refresh_token(jti, user_id)
		except TokenStorageException as e:
			raise e
		except Exception as e:
			raise InvalidDeleteRefresh() from e

	def delete_all_refresh(self, user_id: UUID) -> bool:
		try:
			return self._token_storage.delete_all_refresh_tokens(user_id)
		except TokenStorageException as e:
			raise e
		except Exception as e:
			raise InvalidDeleteAllRefresh() from e

	def exists_refresh(self, jti: str) -> bool:
		try:
			return self._token_storage.exists_refresh_token(jti)
		except TokenStorageException as e:
			raise e
		except Exception as e:
			raise InvalidExistsRefresh() from e
