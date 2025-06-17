from abc import ABC, abstractmethod
from typing import Dict
from uuid import UUID


class JWT(ABC):
    @abstractmethod
    def create_access_token(self, user_id: UUID, username: str) -> str:
        """
        Генерирует JWT access-token, срок жизни ~10–15 минут.

        :param user_id: UUID
        :param username: str
	    :raise InvalidCreateAccessToken: Если не удалось создать access токен
        """
        ...

    @abstractmethod
    def create_refresh_token(self, user_id: UUID) -> tuple:
        """
        Генерирует JWT refresh-token c jti, срок жизни ~7 дней.

        :param user_id: UUID
	    :raise InvalidCreateRefreshToken: Если не удалось создать refresh токен
        """
        ...

    @abstractmethod
    def decode(self, token: str) -> dict:
        """
        Расшифровывает и верифицирует любой токен.

        :param token: str
	    :raise InvalidDecode: Если не удалось расшифровать токен
        """
        ...
