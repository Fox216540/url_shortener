from uuid import UUID
from datetime import datetime
from typing import List
from src.domain.message.models.message import Message
from src.domain.message.repositories.message_repo import MessageRepository


class MessageService:
	def __init__(self, repo: MessageRepository):
		self._repo = repo

	def save_message(self, room_id: UUID, sender: str, content: str) -> Message:
		message = Message(
			room_id=room_id,
			sender=sender,
			content=content
		)
		return self._repo.save(message)

	def get_messages_by_date(self, first_date: datetime, last_date: datetime, room_id: UUID) -> List[Message]:
		return self._repo.get_by_date(first_date=first_date, last_date=last_date, room_id=room_id)

	def delete_message(self, message_id: UUID) -> bool:
		return self._repo.delete(message_id=message_id)

