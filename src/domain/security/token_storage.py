from abc import ABC, abstractmethod


class TokenStorage(ABC):
	@abstractmethod
	def save_refresh_token(self, jti: str) -> bool:
		"""
		Сохраняет refresh токен с идентификатором jti.
		"""
		...

	@abstractmethod
	def exists_refresh_token(self, jti: str) -> bool:
		"""
		Проверяет существование refresh токен с идентификатором jti.
		"""
		...

	@abstractmethod
	def delete_refresh_token(self, jti: str) -> bool:
		"""
		Удаляет refresh токен с идентификатором jti.
		"""
		...
