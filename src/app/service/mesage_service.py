from uuid import UUID
from datetime import datetime
from typing import List
from src.domain.message.models.message import Message
from src.domain.message.repositories.message_repo import MessageRepository
from src.app.service.user_service import UserService


class MessageService:
	def __init__(self, repo: MessageRepository, user_service: UserService):
		self._repo = repo
		self._user_service = user_service

	def save_message(self, room_id: UUID, sender: str, content: str) -> Message:
		message = Message(
			room_id=room_id,
			sender=sender,
			content=content
		)
		return self._repo.save(message)

	def get_messages_by_date(self, first_date: datetime, last_date: datetime, room_id: UUID) -> List[Message]:
		return self._repo.get_by_date(first_date=first_date, last_date=last_date, room_id=room_id)

	def delete_message(self, message_id: UUID, user_id: str, room_id: UUID) -> bool:
		return self._repo.delete(message_id=message_id, sender=user_id, room_id=room_id)

	def resolve_username(self, sender: str) -> str:
		if not sender or sender.startswith("anon_"):
			return "anon"
		try:
			user = self._user_service.get_user_by_id(UUID(sender))
			return user.username if user else "anon"
		except Exception:
			return "anon"

	def change_message(self, user_id: str, room_id: UUID, message_id: UUID, new_content: str) -> Message:
		return self._repo.change_text(sender=user_id, room_id=room_id, message_id=message_id, new_content=new_content)
