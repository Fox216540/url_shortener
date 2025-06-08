from abc import ABC, abstractmethod
from src.domain.message.models.message import Message
from typing import Optional, List
from datetime import datetime
from uuid import UUID


class MessageRepository(ABC):
	@abstractmethod
	def save(self, message: Message) -> Optional[Message]:
		"""Добавляет сообщение"""
		...

	@abstractmethod
	def get_by_date(self, first_date: datetime, last_date: datetime, room_id: UUID) -> Optional[List[Message]]:
		"""Возвращает сообщения с даты по дате"""
		...

	@abstractmethod
	def delete(self, message_id: UUID) -> Optional[bool]:
		"""Удаляет сообщение по message_id"""
		...
