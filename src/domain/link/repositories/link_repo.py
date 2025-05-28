# type InterfaceName interface {
#     funcname()...
# }
from abc import ABC, abstractmethod
from src.domain.link.models.link import Link
from typing import Optional


class LinkRepository(ABC):
	@abstractmethod
	def create(self, link: Link) -> Link:
		"""Добавляет линк"""
		pass

	@abstractmethod
	def get_by_id(self, link_id: int) -> Optional[Link]:
		"""Возвращает линк по его id"""
		pass

	@abstractmethod
	def get_by_alias(self, alias: str) -> Optional[Link]:
		"""Возвращает линк по его alias"""
		pass
