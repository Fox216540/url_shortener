from abc import ABC, abstractmethod
from typing import Dict
from uuid import UUID


class JWT(ABC):
    @abstractmethod
    def create_access_token(self, user_id: UUID, username: str) -> str:
        """
        Генерирует JWT access-token, срок жизни ~10–15 минут.
        """
        ...

    @abstractmethod
    def create_refresh_token(self, user_id: UUID) -> tuple:
        """
        Генерирует JWT refresh-token c jti, срок жизни ~7 дней.
        """
        ...

    @abstractmethod
    def decode(self, token: str) -> dict:
        """
        Расшифровывает и верифицирует любой токен.
        """
        ...
