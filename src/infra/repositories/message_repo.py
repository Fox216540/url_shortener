from datetime import datetime
from uuid import UUID
from typing import List
from sqlalchemy import select
from typing import Optional
from src.domain.message.models.message import Message
from src.domain.message.repositories.message_repo import MessageRepository
from src.infra.database import get_session
from src.infra.repositories.models.message_model import MessageORM
from src.infra.repositories.exceptions import message_exception


class MessageRepositoryImpl(MessageRepository):
	def save(self, message: Message) -> Optional[Message]:
		try:
			with get_session() as session:
				new_message = MessageORM(
					room_id=message.room_id,
					sender=message.sender,
					content=message.content,
				)
				session.add(new_message)
				session.commit()
				session.refresh(new_message)
				return Message.from_orm(new_message)
		except Exception as e:
			raise message_exception.InvalidSave() from e

	def get_by_date(
			self, first_date: datetime, last_date: datetime, room_id: UUID
	) -> Optional[List[Message]]:
		try:
			with get_session() as session:
				stmt = (
					select(MessageORM)
					.where(
						MessageORM.room_id == room_id,
						MessageORM.created_at >= first_date,
						MessageORM.created_at <= last_date
					)
					.order_by(MessageORM.created_at.asc())
				)
				result = session.scalars(stmt).all()
				if not result:
					raise message_exception.MessagesNotExist()
				return [Message.from_orm(msg) for msg in result]
		except message_exception.MessagesNotExist as e:
			raise e
		except Exception as e:
			raise message_exception.InvalidGetMessagesByDate() from e

	def delete(self, message_id: UUID, sender: str, room_id: UUID) -> Optional[bool]:
		try:
			with get_session() as session:
				message = session.query(MessageORM).filter(
					MessageORM.uuid_id == message_id,
					MessageORM.sender == sender,
					MessageORM.room_id == room_id
				).first()
				if not message:
					raise message_exception.MessagesNotExist()
				session.delete(message)
				session.commit()
				return True
		except message_exception.MessagesNotExist as e:
			raise e
		except Exception as e:
			raise message_exception.InvalidDelete() from e

	def change_text(self, message_id: UUID, sender: str, room_id: UUID, new_content: str) -> Optional[Message]:
		try:
			with get_session() as session:
				message = session.query(MessageORM).filter(
					MessageORM.uuid_id == message_id,
					MessageORM.sender == sender,
					MessageORM.room_id == room_id
				).first()
				if not message:
					raise message_exception.MessagesNotExist()
				message.content = new_content
				session.commit()
				return Message.from_orm(message)
		except message_exception.MessagesNotExist as e:
			raise e
		except Exception as e:
			raise message_exception.InvalidChangeText() from e
