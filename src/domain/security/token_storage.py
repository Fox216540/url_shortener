from abc import ABC, abstractmethod
from uuid import UUID


class TokenStorage(ABC):
	@abstractmethod
	def save_refresh_token(self, jti: str, user_id: UUID) -> bool:
		"""
		Сохраняет refresh токен с идентификатором jti и добавляет в группу по user_id.
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

	@abstractmethod
	def delete_all_refresh_tokens(self, user_id: UUID) -> bool:
		"""
		Удаляет все refresh токен с идентификатором jti по user_id.
		"""
		...
