from src.domain.user.models.user import User
from src.domain.user.repositories.user_repo import UserRepository
from typing import Optional
from src.infra.database import get_session
from src.infra.repositories.models.user_model import UserORM


class UserRepositoryImpl(UserRepository):
    def create(self, user: User) -> bool:
        with get_session() as session:
            new_link = UserORM(
                name=user.name,
                mail=user.mail,
                username=user.username,
                password=user.password,
            )

            session.add(new_link)
            session.commit()
            return True

    def get_by_mail(self, mail: str) -> Optional[User]:
        with get_session() as session:
            user = session.query(UserORM).filter(UserORM.mail == mail).first()
            if not user:
                return None
            return User.from_orm(user)


# '''
# EXAMPLE:
# '''
#
# class Figure(ABC):
#     square: float
#
#     @abstractmethod
#     def calc_square(self):
#         pass
#
# class Rectangle(Figure):
#     def calc_square(self):
#         pass
#
# class Triangle(Figure):
#     def calc_square(self):
#         pass