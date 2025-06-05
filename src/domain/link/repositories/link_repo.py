from abc import ABC, abstractmethod
from src.domain.link.models.link import Link
from typing import Optional
from uuid import UUID
from typing import List


class LinkRepository(ABC):
	@abstractmethod
	def create(self, link: Link) -> Link:
		"""Добавляет линк"""
		...

	@abstractmethod
	def get_by_id(self, link_id: int, user_id: UUID = None) -> Optional[Link]:
		"""Возвращает линк по id"""
		...

	@abstractmethod
	def get_by_alias(self, alias: str, user_id: UUID = None) -> Optional[Link]:
		"""Возвращает линк по alias"""
		...

	@abstractmethod
	def get_all_by_owner_id(self, user_id: UUID) -> Optional[List[Link]]:
		"""Возвращает линки по owner_id"""
		...

	@abstractmethod
	def delete_link_by_owner_id_by_link_id(self, link_id: int, user_id: UUID) -> Optional[bool]:
		"""Удаление ссылки по id"""
		...

	@abstractmethod
	def delete_link_by_owner_id_by_alias(self, alias: str, user_id: UUID) -> Optional[bool]:
		"""Удаление ссылки по alias"""
		...

	@abstractmethod
	def delete_all_by_owner_id(self, user_id: UUID) -> Optional[bool]:
		"""Удаление всех ссылок"""
		...
