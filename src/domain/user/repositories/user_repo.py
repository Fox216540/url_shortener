from abc import ABC, abstractmethod
from src.domain.user.models.user import User
from typing import Optional


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> Optional[User]:
        """Добавляет юзера"""
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        """Возвращает пользователя по его почте"""
        pass

    @abstractmethod
    def exists_by_email(self, email: str) -> Optional[bool]:
        """Проверяет существование пользователя с указанным email"""
        pass
