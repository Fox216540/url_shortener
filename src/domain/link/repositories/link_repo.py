from abc import ABC, abstractmethod
from src.domain.link.models.link import Link
from typing import Optional
from uuid import UUID

class LinkRepository(ABC):
	@abstractmethod
	def create(self, link: Link) -> Link:
		"""Добавляет линк"""
		pass

	@abstractmethod
	def get_by_id(self, link_id: int, user_id: UUID = None) -> Optional[Link]:
		"""Возвращает линк по id"""
		pass

	@abstractmethod
	def get_by_alias(self, alias: str, user_id: UUID = None) -> Optional[Link]:
		"""Возвращает линк по alias"""
		pass
