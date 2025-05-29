from abc import ABC, abstractmethod
from typing import Dict
from uuid import UUID


class JWT(ABC):
    @abstractmethod
    def create_access_token(self, user_id: UUID, username: str) -> str:
        """
        Генерирует JWT access-token, срок жизни ~10–15 минут.
        """
        pass

    @abstractmethod
    def create_refresh_token(self, user_id: UUID) -> str:
        """
        Генерирует JWT refresh-token, срок жизни ~7 дней.
        """
        pass

    @abstractmethod
    def decode(self, token: str) -> dict:
        """
        Расшифровывает и верифицирует любой токен.
        """
        pass

    @abstractmethod
    def refresh(self, refresh_token: str, username: str) -> Dict[str, str]:
        """
        Принимает действительный refresh-токен и действительный username
        и возвращает (new_access_token, new_refresh_token).
        """
        pass
