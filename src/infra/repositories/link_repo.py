from src.domain.link.models.link import Link
from src.domain.link.repositories.link_repo import LinkRepository
from typing import Optional
from src.infra.database import get_session
from src.infra.repositories.models.link_model import LinkORM
from uuid import UUID

class LinkRepositoryImpl(LinkRepository):
	def create(self, link: Link) -> Link:
		with get_session() as session:
			new_link = LinkORM(
				original_url=link.original_url,
				owner_id=str(link.owner_id) if link.owner_id else None,
				alias=link.alias,
			)

			session.add(new_link)
			session.commit()
			session.refresh(new_link)
			return Link.from_orm(new_link)

	def get_by_id(self, link_id, user_id: UUID = None) -> Optional[Link]:
		with get_session() as session:
			query = session.query(LinkORM).filter(LinkORM.id == link_id)
			if user_id is not None:
				query = query.filter(LinkORM.owner_id == user_id)
			link = query.first()
			return Link.from_orm(link) if link else None

	def get_by_alias(self, alias: str, user_id: UUID = None) -> Optional[Link]:
		with get_session() as session:
			query = session.query(LinkORM).filter(LinkORM.alias == alias)
			if user_id is not None:
				query = query.filter(LinkORM.owner_id == user_id)
			link = query.first()
			return Link.from_orm(link) if link else None
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
