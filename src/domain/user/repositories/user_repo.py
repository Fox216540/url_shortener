from abc import ABC, abstractmethod
from src.domain.user.models.user import User
from typing import Optional
from uuid import UUID

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> Optional[User]:
        """Добавляет юзера"""
        pass

    @abstractmethod
    def get_by_id(self, user_id: UUID) -> Optional[User]:
        """Возвращает пользователя по его id"""
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> Optional[User]:
        """Возвращает пользователя по его id"""
        pass

    @abstractmethod
    def exists_by_email(self, email: str) -> Optional[bool]:
        """Проверяет существование пользователя с указанным email"""
        pass

    @abstractmethod
    def exists_by_username(self, username: str) -> Optional[bool]:
        """Проверяет существование пользователя с указанным username"""
        pass

    @abstractmethod
    def change_password(self, user_id: UUID, password: str) -> Optional[User]:
        """Меняет пароль у пользователя"""
        pass

    @abstractmethod
    def change_username(self, user_id: UUID, username: str) -> Optional[User]:
        """Меняет username у пользователя"""
        pass

    @abstractmethod
    def change_name(self, user_id: UUID, name: str) -> Optional[User]:
        """Меняет username у пользователя"""
        pass

    @abstractmethod
    def change_email(self, user_id: UUID, email: str) -> Optional[User]:
        """Меняет username у пользователя"""
        pass
