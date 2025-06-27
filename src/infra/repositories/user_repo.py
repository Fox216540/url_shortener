from uuid import UUID
from sqlalchemy import exists
from src.domain.user.models.user import User
from src.domain.user.repositories.user_repo import UserRepository
from src.infra.database import get_session
from src.infra.repositories.exceptions import user_exception
from src.infra.repositories.models.user_model import UserORM
from src.logger import error_logger

class UserRepositoryImpl(UserRepository):
	def save(self, user: User) -> User:
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
			raise user_exception.InfraInvalidCreateUser() from e

	def get_by_id(self, user_id: UUID) -> User:
		try:
			with get_session() as session:
				user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
				if not user:
					raise user_exception.InfraUserNotExists()
				return User.from_orm(user)
		except user_exception.InfraUserNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InfraInvalidGetUserById() from e

	def get_by_username(self, username: str) -> User:
		try:
			with get_session() as session:
				user = session.query(UserORM).filter(UserORM.username == username).first()
				if not user:
					raise user_exception.InfraUserNotExists()
				return User.from_orm(user)
		except user_exception.InfraUserNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InfraInvalidGetUserByUsername() from e

	def get_by_email(self, email: str) -> User:
		try:
			with get_session() as session:
				user = session.query(UserORM).filter(UserORM.email == email).first()
				if not user:
					raise user_exception.InfraUserNotExists()
				return User.from_orm(user)
		except user_exception.InfraUserNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InfraInvalidGetUserByEmail() from e

	def exists_by_email(self, email: str) -> bool:
		try:
			with get_session() as session:
				return session.query(
					exists().where(UserORM.email == email)
				).scalar()
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InfraInvalidExistingUser() from e

	def exists_by_username(self, username: str) -> bool:
		try:
			with get_session() as session:
				return session.query(
					exists().where(UserORM.username == username)
				).scalar()
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InfraInvalidExistingUser() from e

	def change_password(self, user_id: UUID, password: str) -> User:
		try:
			with get_session() as session:
				user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
				if not user:
					raise user_exception.InfraUserNotExists()
				user.password = password
				session.commit()
				return User.from_orm(user)
		except user_exception.InfraUserNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InfraInvalidChangePassword() from e

	def change_username(self, user_id: UUID, username: str) -> User:
		try:
			with get_session() as session:
				user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
				if not user:
					raise user_exception.InfraUserNotExists()
				user.username = username
				session.commit()
				return User.from_orm(user)
		except user_exception.InfraUserNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InfraInvalidChangeUsername() from e

	def change_name(self, user_id: UUID, name: str) -> User:
		try:
			with get_session() as session:
				user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
				if not user:
					raise user_exception.InfraUserNotExists()
				user.name = name
				session.commit()
				return User.from_orm(user)
		except user_exception.InfraUserNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InfraInvalidChangeName() from e

	def change_email(self, user_id: UUID, email: str) -> User:
		try:
			with get_session() as session:
				user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
				if not user:
					raise user_exception.InfraUserNotExists()
				user.email = email
				session.commit()
				return User.from_orm(user)
		except user_exception.InfraUserNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InfraInvalidChangeEmail() from e

	def delete(self, user_id: UUID) -> bool:
		try:
			with get_session() as session:
				user = session.query(UserORM).filter(UserORM.uuid_id == user_id).first()
				if not user:
					raise user_exception.InfraUserNotExists()
				session.delete(user)
				session.commit()
				return True
		except user_exception.InfraUserNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise user_exception.InfraInvalidDelete() from e

