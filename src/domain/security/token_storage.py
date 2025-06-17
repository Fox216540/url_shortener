from abc import ABC, abstractmethod
from uuid import UUID
#TODO: Добавить полное описание

class TokenStorage(ABC):
	@abstractmethod
	def save_refresh_token(self, jti: str, user_id: UUID) -> bool:
		"""
		Сохраняет refresh токен с идентификатором jti и добавляет в группу по user_id.

		:param jti: str
		:param user_id: UUID
	    :raise InvalidSaveRefreshToken: Если не удалось сохранить refresh токен
		"""
		...

	@abstractmethod
	def exists_refresh_token(self, jti: str) -> bool:
		"""
		Проверяет существование refresh токен с идентификатором jti.

        :param jti: str
	    :raise InvalidExistsRefreshToken: Если не удалось проверить существование токена
		"""
		...

	@abstractmethod
	def delete_refresh_token(self, jti: str, user_id: UUID) -> bool:
		"""
		Удаляет refresh токен с идентификатором jti и user_id.

		:param jti: str
		:param user_id: UUID
	    :raise InvalidDeleteRefreshToken: Если не удалось удалить токен
	    :raise RefreshTokenNotExists: Если токена не существует
		"""
		...

	@abstractmethod
	def delete_all_refresh_tokens(self, user_id: UUID) -> bool:
		"""
		Удаляет все refresh токены с идентификатором jti по user_id.

		:param user_id: UUID
	    :raise InvalidCreateAccessToken: Если не удалось создать access токен
	    :raise RefreshTokensNotExist: Если токенов не существует
		"""
		...
