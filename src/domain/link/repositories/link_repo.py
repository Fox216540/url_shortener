from abc import ABC, abstractmethod
from src.domain.link.models.link import Link
from uuid import UUID
from typing import List

class LinkRepository(ABC):
	@abstractmethod
	def create(self, link: Link) -> Link:
		"""
		Добавляет линк

		:param link: Link
		:raise InvalidCreateLink: Если не удалось добавить
		"""
		...

	@abstractmethod
	def check_short_code(self, short_code: str) -> bool:
		"""
		Проверка на существование

		:param short_code: str
		:raise InvalidCheckShortCode: Если не удалось проверить
		"""
		...

	@abstractmethod
	def get_by_short_code(self, short_code: str) -> Link:
		"""
		Возвращает линк по short_code

		:param short_code: str
		:raise InvalidGetLink: Если не удалось вернуть ссылку
		:raise LinkNotExists: Если ссылка не найдена
		"""
		...

	@abstractmethod
	def get_by_alias(self, alias: str, owner_id: UUID = None) -> Link:
		"""
		Возвращает линк по alias

		:param alias: str
		:param owner_id: UUID = None
		:raise InvalidGetLink: Если не удалось вернуть ссылку
		:raise LinkNotExists: Если ссылка не найдена
		"""
		...

	@abstractmethod
	def get_all_by_owner_id(self, owner_id: UUID) -> List[Link]:
		"""
		Возвращает все ссылки по owner_id

		:param owner_id: UUID
		:raise InvalidGetAllLinks: Если не удалось вернуть все ссылки
		:raise LinksNotExist: Если ссылки не найдены
		"""
		...

	@abstractmethod
	def delete_link_by_owner_id_by_link_short_code(self, short_code: str, owner_id: UUID) -> bool:
		"""
		Удаление ссылки по short_code

		:param short_code: str
		:param owner_id: UUID
		:raise InvalidGetUserById: Если не удалось удалить ссылку
		:raise LinkNotExists: Если ссылка не найдена
		"""
		...

	@abstractmethod
	def delete_link_by_owner_id_by_alias(self, alias: str, owner_id: UUID) -> bool:
		"""
		Удаление ссылки по alias

		:param alias: str
		:param owner_id: UUID
		:raise InvalidDeleteLink: Если не удалось удалить ссылку
		:raise LinkNotExists: Если ссылка не найдена
		"""
		...

	@abstractmethod
	def delete_all_by_owner_id(self, owner_id: UUID) -> bool:
		"""
		Удаление всех ссылок

		:param owner_id: UUID
		:raise InvalidDeleteAllLinks: Если не удалось удалить все ссылки
		:raise LinksNotExist: Если ссылки не найдены
		"""
		...

