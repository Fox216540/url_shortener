from datetime import datetime
from src.domain.message.models.message import Message
from src.domain.message.repositories.message_repo import MessageRepository
from typing import Optional
from src.infra.database import get_session
from src.infra.repositories.models.message_model import MessageORM
from uuid import UUID
from typing import List
from sqlalchemy import select


class MessageRepositoryImpl(MessageRepository):
	def save(self, message: Message) -> Optional[Message]:
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

	def get_by_date(
			self, first_date: datetime, last_date: datetime, room_id: UUID
	) -> Optional[List[Message]]:
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
			return [Message.from_orm(msg) for msg in result] if result else None

	def delete(self, message_id: UUID, sender: str, room_id: UUID) -> Optional[bool]:
		with get_session() as session:
			message = session.query(MessageORM).filter(
				MessageORM.uuid_id == message_id,
				MessageORM.sender == sender,
				MessageORM.room_id == room_id
			).first()
			if not message:
				return None
			session.delete(message)
			session.commit()
			return True

	def change_text(self, message_id: UUID, sender: str, room_id: UUID, new_content: str) -> Optional[Message]:
		with get_session() as session:
			message = session.query(MessageORM).filter(
				MessageORM.uuid_id == message_id,
				MessageORM.sender == sender,
				MessageORM.room_id == room_id
			).first()
			if not message:
				return None
			message.content = new_content
			session.commit()
			return Message.from_orm(message)
