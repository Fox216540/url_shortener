from abc import ABC, abstractmethod
from src.domain.message.models.message import Message
from typing import Optional, List
from datetime import datetime
from uuid import UUID
#TODO: Добавить полное описание

class MessageRepository(ABC):
	@abstractmethod
	def save(self, message: Message) -> Optional[Message]:
		"""
		Добавляет сообщение

		:param message: Message
	    :raise InvalidSave: Если не удалось добавить сообщение
		"""
		...

	@abstractmethod
	def get_by_date(self, first_date: datetime, last_date: datetime, room_id: UUID) -> Optional[List[Message]]:
		"""
		Возвращает сообщения с даты по дате

		:param first_date: datetime
		:param last_date: datetime
		:param room_id: UUID
		:raise MessagesNotExist: Если нет сообщений
	    :raise InvalidGetMessagesByDate: Если не удалось получить сообщения с даты по дате
		"""
		...

	@abstractmethod
	def delete(self, message_id: UUID, sender: str, room_id: UUID) -> Optional[bool]:
		"""
		Удаляет сообщение по message_id и sender

		:param message_id: UUID
		:param sender: str
		:param room_id: UUID
		:raise MessageNotExists: Если нет сообщения
	    :raise InvalidDelete: Если не удалось удалить сообщение
		"""
		...

	@abstractmethod
	def change_text(self, message_id: UUID, sender: str, room_id: UUID, new_content: str) -> Optional[Message]:
		"""
		Меняет текст сообщения по message_id, room_id и sender

		:param message_id: UUID
		:param sender: str
		:param room_id: UUID
		:param new_content: str
	    :raise MessageNotExists: Если нет сообщения
	    :raise InvalidChangeText: Если не удалось поменять текст сообщения
		"""
		...
