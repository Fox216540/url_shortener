from uuid import UUID
from sqlalchemy import exists
from typing import Optional
from src.domain.user.models.user import User
from src.domain.user.repositories.user_repo import UserRepository
from src.infra.database import get_session
from src.infra.repositories.exceptions import user_exception
from src.infra.repositories.models.user_model import UserORM
from src.logger import error_logger


class UserRepositoryImpl(UserRepository):
	def save(self, user: User) -> Optional[User]:
		try:
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
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InvalidCreateUser()

	def get_by_id(self, user_id: UUID) -> Optional[User]:
		try:
			with get_session() as session:
				user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
				if not user:
					raise user_exception.UserNotExists()
				return User.from_orm(user)
		except user_exception.UserNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InvalidGetUserById()

	def get_by_username(self, username: str) -> Optional[User]:
		try:
			with get_session() as session:
				user = session.query(UserORM).filter(UserORM.username == username).first()
				if not user:
					raise user_exception.UserNotExists()
				return User.from_orm(user)
		except user_exception.UserNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InvalidGetUserByUsername()

	def get_by_email(self, email: str) -> Optional[User]:
		try:
			with get_session() as session:
				user = session.query(UserORM).filter(UserORM.email == email).first()
				if not user:
					raise user_exception.UserNotExists()
				return User.from_orm(user)
		except user_exception.UserNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InvalidGetUserByEmail()

	def exists_by_email(self, email: str) -> Optional[bool]:
		try:
			with get_session() as session:
				return session.query(
					exists().where(UserORM.email == email)
				).scalar()
		except Exception as e:
			raise user_exception.InvalidExistingUser()

	def exists_by_username(self, username: str) -> Optional[bool]:
		try:
			with get_session() as session:
				return session.query(
					exists().where(UserORM.username == username)
				).scalar()
		except Exception as e:
			raise user_exception.InvalidExistingUser()

	def change_password(self, user_id: UUID, password: str) -> Optional[User]:
		try:
			with get_session() as session:
				user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
				if not user:
					raise user_exception.UserNotExists()
				user.password = password
				session.commit()
				return User.from_orm(user)
		except user_exception.UserNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InvalidChangePassword() from e

	def change_username(self, user_id: UUID, username: str) -> Optional[User]:
		try:
			with get_session() as session:
				user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
				if not user:
					raise user_exception.UserNotExists()
				user.username = username
				session.commit()
				return User.from_orm(user)
		except user_exception.UserNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InvalidChangeUsername() from e

	def change_name(self, user_id: UUID, name: str) -> Optional[User]:
		try:
			with get_session() as session:
				user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
				if not user:
					raise user_exception.UserNotExists()
				user.name = name
				session.commit()
				return User.from_orm(user)
		except user_exception.UserNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InvalidChangeName() from e

	def change_email(self, user_id: UUID, email: str) -> Optional[User]:
		try:
			with get_session() as session:
				user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
				if not user:
					raise user_exception.UserNotExists()
				user.email = email
				session.commit()
				return User.from_orm(user)
		except user_exception.UserNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InvalidChangeEmail() from e

	def delete(self, user_id: UUID) -> Optional[bool]:
		try:
			with get_session() as session:
				user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
				if not user:
					raise user_exception.UserNotExists()
				session.delete(user)
				session.commit()
				return True
		except user_exception.UserNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InvalidDelete() from e

