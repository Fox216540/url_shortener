from jose import jwt
from datetime import datetime, timedelta
from src.domain.security.jwt import JWT
from uuid import UUID
from uuid import uuid4
from settings import ACCESS_TOKEN_TIME, REFRESH_TOKEN_TIME
from src.infra.security.exceptions import jwt_exception
from src.logger import error_logger


class JWTImpl(JWT):
	def __init__(self, secret: str):
		self.secret = secret

	def create_access_token(self, user_id: UUID, username: str) -> str:
		try:
			payload = {"sub": str(user_id),
			           "type": "access",
			           "username": username,
			           "exp": datetime.now() + timedelta(seconds=ACCESS_TOKEN_TIME)}
			return jwt.encode(payload, self.secret, algorithm="HS256")
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise jwt_exception.InfraInvalidCreateAccessToken() from e

	def create_refresh_token(self, user_id: UUID) -> tuple:
		try:
			jti = str(uuid4())
			payload = {"sub": str(user_id),
			           "jti": jti,
			           "type": "refresh",
			           "exp": datetime.now() + timedelta(seconds=REFRESH_TOKEN_TIME)}
			return jwt.encode(payload, self.secret, algorithm="HS256"), jti
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise jwt_exception.InfraInvalidCreateRefreshToken() from e

	def decode(self, token: str) -> dict:
		try:
			return jwt.decode(token, self.secret, algorithms=["HS256"])
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise jwt_exception.InfraInvalidDecode() from e
