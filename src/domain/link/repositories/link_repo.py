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
	def check_short_code(self, short_code: str) -> Optional[bool]:
		"""Проверка на существование"""
		...

	@abstractmethod
	def get_by_short_code(self, short_code: str) -> Optional[Link]:
		"""Возвращает линк по short_code"""
		...

	@abstractmethod
	def get_by_alias(self, alias: str, owner_id: UUID = None) -> Optional[Link]:
		"""Возвращает линк по alias"""
		...

	@abstractmethod
	def get_all_by_owner_id(self, owner_id: UUID) -> Optional[List[Link]]:
		"""Возвращает линки по owner_id"""
		...

	@abstractmethod
	def delete_link_by_owner_id_by_link_short_code(self, short_code: str, owner_id: UUID) -> Optional[bool]:
		"""Удаление ссылки по short_code"""
		...

	@abstractmethod
	def delete_link_by_owner_id_by_alias(self, alias: str, owner_id: UUID) -> Optional[bool]:
		"""Удаление ссылки по alias"""
		...

	@abstractmethod
	def delete_all_by_owner_id(self, owner_id: UUID) -> Optional[bool]:
		"""Удаление всех ссылок"""
		...

