from abc import ABC, abstractmethod
from src.domain.user.models.user import User
from typing import Optional


class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> Optional[bool]:
        """Добавляет юзера"""
        pass

    @abstractmethod
    def get_by_mail(self, mail: str) -> Optional[User]:
        """Возвращает пользователя по его id"""
        pass
