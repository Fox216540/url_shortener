from abc import ABC, abstractmethod


class Health(ABC):
	@abstractmethod
	def check_health_db(self) -> bool:
		"""
		Проверяет состояние базы данных

		:raise InvalidDbConnection: Если возникли проблемы с подключением к базе данных
		"""
		...

	@abstractmethod
	def check_health_token_storage(self) -> bool:
		"""
		Проверяет состояние хранилища токенов

		:raise InvalidTSConnection: Если возникли проблемы с подключением к хранилищу токенов
		"""
		...

