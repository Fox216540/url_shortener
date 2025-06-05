from src.infra.redis_conn import get_redis
from src.domain.security.token_storage import TokenStorage
from settings import REFRESH_TOKEN_TIME


class TokenStorageImpl(TokenStorage):
	def save_refresh_token(self, jti: str) -> bool:
		with get_redis() as client:
			return client.set(jti, "1", ex=REFRESH_TOKEN_TIME)

	def exists_refresh_token(self, jti: str) -> bool:
		with get_redis() as client:
			return client.exists(jti) == 1

	def delete_refresh_token(self, jti: str) -> bool:
		with get_redis() as client:
			return client.delete(jti) == 1

