from uuid import UUID
from sqlalchemy import exists
from src.domain.user.models.user import User
from src.domain.user.repositories.user_repo import UserRepository
from typing import Optional
from src.infra.database import get_session
from src.infra.repositories.models.user_model import UserORM


class UserRepositoryImpl(UserRepository):
	def save(self, user: User) -> Optional[User]:
		with get_session() as session:
			new_user = UserORM(
				name=user.name,
				email=user.email,
				username=user.username,
				password=user.password,
			)

			session.add(new_user)
			session.commit()
			session.refresh(new_user)
			return User.from_orm(new_user)

	def get_by_id(self, user_id: UUID) -> Optional[User]:
		with get_session() as session:
			user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
			if not user:
				return None
			return User.from_orm(user)

	def get_by_username(self, username: str) -> Optional[User]:
		with get_session() as session:
			user = session.query(UserORM).filter(UserORM.username == username).first()
			if not user:
				return None
			return User.from_orm(user)

	def get_by_email(self, email: str) -> Optional[User]:
		with get_session() as session:
			user = session.query(UserORM).filter(UserORM.email == email).first()
			if not user:
				return None
			return User.from_orm(user)

	def exists_by_email(self, email: str) -> Optional[bool]:
		with get_session() as session:
			return session.query(
				exists().where(UserORM.email == email)
			).scalar()

	def exists_by_username(self, username: str) -> Optional[bool]:
		with get_session() as session:
			return session.query(
				exists().where(UserORM.username == username)
			).scalar()

	def change_password(self, user_id: UUID, password: str) -> Optional[User]:
		with get_session() as session:
			user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
			if not user:
				return None
			user.password = password
			session.commit()
			return User.from_orm(user)

	def change_username(self, user_id: UUID, username: str) -> Optional[User]:
		with get_session() as session:
			user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
			if not user:
				return None
			user.username = username
			session.commit()
			return User.from_orm(user)

	def change_name(self, user_id: UUID, name: str) -> Optional[User]:
		with get_session() as session:
			user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
			if not user:
				return None
			user.name = name
			session.commit()
			return User.from_orm(user)

	def change_email(self, user_id: UUID, email: str) -> Optional[User]:
		with get_session() as session:
			user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
			if not user:
				return None
			user.email = email
			session.commit()
			return User.from_orm(user)

	def delete(self, user_id: UUID) -> Optional[bool]:
		with get_session() as session:
			user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
			if not user:
				return None
			session.delete(user)
			session.commit()
			return True
