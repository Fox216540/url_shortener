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

    def get_by_email(self, email: str) -> Optional[User]:
        with get_session() as session:
            user = session.query(UserORM).filter(UserORM.email == email).first()
            if not user:
                return None
            return User.from_orm(user)

    def exists_by_email(self, email: str) -> Optional[bool]:
        with get_session() as session:
            exists = session.query(
                session.query(UserORM)
                .filter(UserORM.email == email)
                .exists()
            ).scalar()
        return bool(exists)



