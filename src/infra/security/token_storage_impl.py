from uuid import UUID
from src.infra.redis_conn import get_redis
from src.domain.security.token_storage import TokenStorage
from settings import REFRESH_TOKEN_TIME
from src.infra.security.exceptions import token_storage_exception
from src.logger import error_logger


class TokenStorageImpl(TokenStorage):
	def save_refresh_token(self, jti: str, user_id: UUID) -> bool:
		try:
			with get_redis() as client:
				return (
						bool(client.sadd(f"user:{user_id}:refresh_tokens", jti))
						and
						bool(client.set(jti, str(user_id), ex=REFRESH_TOKEN_TIME))
				)
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise token_storage_exception.InfraInvalidSaveRefreshToken() from e


	def exists_refresh_token(self, jti: str) -> bool:
		try:
			with get_redis() as client:
				return client.exists(jti) == 1
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise token_storage_exception.InfraInvalidExistsRefreshToken() from e

	def delete_refresh_token(self, jti: str, user_id: UUID) -> bool:
		try:
			with get_redis() as client:
				client.delete(jti)
				removed = client.srem(f"user:{user_id}:refresh_tokens", jti)
				if not removed:
					raise token_storage_exception.InfraRefreshTokenNotExists()
				return removed
		except token_storage_exception.InfraRefreshTokenNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise token_storage_exception.InfraInvalidDeleteRefreshToken() from e

	def delete_all_refresh_tokens(self, user_id: UUID) -> bool:
		try:
			with get_redis() as client:
				jtis = client.smembers(f"user:{user_id}:refresh_tokens")
				if not jtis:
					raise token_storage_exception.InfraRefreshTokensNotExist()
				keys_to_delete = list(jtis) + [f"user:{user_id}:refresh_tokens"]
				client.delete(*keys_to_delete)
				return True
		except token_storage_exception.RefreshTokensNotExist as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise token_storage_exception.InfraInvalidDeleteAllRefreshTokens() from e