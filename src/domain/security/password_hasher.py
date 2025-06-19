from abc import ABC, abstractmethod


class PasswordHasher(ABC):
	@abstractmethod
	def hash(self, plain: str) -> str:
		"""
		Хэширует пароль

		:param plain: str
		:raise InvalidHash: Если возникли проблемы
		"""
		...

	@abstractmethod
	def verify(self, plain: str, hashed: str) -> bool:
		"""
		Проверяет значение

		:param plain: str
		:param hashed: str
		:raise InvalidVerify: Если возникли проблемы
		"""
		...
