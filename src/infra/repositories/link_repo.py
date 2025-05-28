from src.domain.link.models.link import Link
from src.domain.link.repositories.link_repo import LinkRepository
from typing import Optional
from src.infra.database import get_session
from src.infra.repositories.models.link_model import LinkORM


class LinkRepositoryImpl(LinkRepository):
    def add(self, link: Link) -> Link:
        with get_session() as session:
            new_link = LinkORM(
                original_url=link.original_url,
                owner_id=str(link.owner_id) if link.owner_id else None
            )

            session.add(new_link)
            session.commit()
            session.refresh(new_link)
            return Link.from_orm(new_link)

    def get_by_id(self, link_id) -> Optional[Link]:
        with get_session() as session:
            link = session.query(LinkORM).filter(LinkORM.id == link_id).first()
            if not link:
                return None
            return Link.from_orm(link)


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