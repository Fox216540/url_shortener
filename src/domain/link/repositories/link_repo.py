# type InterfaceName interface {
#     funcname()...
# }
from abc import ABC, abstractmethod
from src.domain.link.models.link import Link
from typing import Optional


class LinkRepository(ABC):
    @abstractmethod
    def add(self, link: Link) -> Link:
        """Добавляет линк"""
        pass

    @abstractmethod
    def get_by_id(self, short_code: str) -> Optional[Link]:
        """Возвращает линк по его сокращённому коду"""
        pass
