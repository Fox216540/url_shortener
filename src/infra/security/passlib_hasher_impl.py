from passlib.context import CryptContext
from src.domain.security.password_hasher import PasswordHasher
from src.infra.security.exceptions import passlib_hasher_exception
from src.logger import error_logger

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasslibHasher(PasswordHasher):
	def hash(self, plain: str) -> str:
		try:
			return pwd_context.hash(plain)
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise passlib_hasher_exception.InfraInvalidHash() from e

	def verify(self, plain: str, hashed: str) -> bool:
		try:
			return pwd_context.verify(plain, hashed)
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise passlib_hasher_exception.InfraInvalidVerify() from e
