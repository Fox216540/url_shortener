from abc import ABC, abstractmethod
from src.domain.user.models.user import User
from typing import Optional
from uuid import UUID

class UserRepository(ABC):
	@abstractmethod
	def save(self, user: User) -> Optional[User]:
		"""
	    Добавляет пользователя.

	    :param user: User
	    :raise InvalidCreateUser: Если не удалось добавить пользователя
        """
		...

	@abstractmethod
	def get_by_id(self, user_id: UUID) -> Optional[User]:
		"""
		Возвращает пользователя по его id

		:param user_id: UUID : ID Пользователя
		:raise InvalidGetUserById: Если не удалось вернуть пользователя по id
		:raise UserNotExists: Если пользователь не найден
		"""
		...

	@abstractmethod
	def get_by_username(self, username: str) -> Optional[User]:
		"""
		Возвращает пользователя по его username

		:param username: str : username Пользователя
		:raise InvalidGetUserByUsername: Если не удалось вернуть пользователя по username
		:raise UserNotExists: Если пользователь не найден
		"""
		...

	@abstractmethod
	def get_by_email(self, email: str) -> Optional[User]:
		"""
		Возвращает пользователя по его id

		:param email: str
		:raise InvalidGetUserByEmail: Если не удалось вернуть пользователя email
		:raise UserNotExists: Если пользователь не найден
		"""
		...

	@abstractmethod
	def exists_by_email(self, email: str) -> Optional[bool]:
		"""
		Проверяет существование пользователя с указанным email

		:param email: str
		:raise InvalidExistingUser: Если не удалось проверить существование по email
		"""
		...

	@abstractmethod
	def exists_by_username(self, username: str) -> Optional[bool]:
		"""
		Проверяет существование пользователя с указанным username

		:param username: str
		:raise InvalidExistingUser: Если не удалось проверить существование по username
		"""
		...

	@abstractmethod
	def change_password(self, user_id: UUID, password: str) -> Optional[User]:
		"""
		Меняет пароль у пользователя

		:param user_id: UUID
		:param password: str
		:raise InvalidChangePassword: Если не удалось поменять пароль
		:raise UserNotExists: Если пользователь не найден
		"""
		...

	@abstractmethod
	def change_username(self, user_id: UUID, username: str) -> Optional[User]:
		"""
		Меняет username у пользователя

		:param user_id: UUID
		:param username: str
		:raise InvalidChangeUsername: Если не удалось поменять username
		:raise UserNotExists: Если пользователь не найден
		"""
		...

	@abstractmethod
	def change_name(self, user_id: UUID, name: str) -> Optional[User]:
		"""
		Меняет name у пользователя

		:param user_id: UUID
		:param name: str
		:raise InvalidChangeName: Если не удалось поменять имя
		:raise UserNotExists: Если пользователь не найден
		"""
		...

	@abstractmethod
	def change_email(self, user_id: UUID, email: str) -> Optional[User]:
		"""
		Меняет email у пользователя

		:param user_id: UUID
		:param email: str
		:raise InvalidChangeEmail: Если не удалось поменять email
		:raise UserNotExists: Если пользователь не найден
		"""
		...

	@abstractmethod
	def delete(self, user_id: UUID) -> Optional[bool]:
		"""
		Удаляет пользователя

		:param user_id: UUID
		:raise InvalidDelete: Если не удалось удалить пользователя
		:raise UserNotExists: Если пользователь не найден
		"""
		...
