from src.domain.link.models.link import Link
from src.domain.link.repositories.link_repo import LinkRepository
from src.infra.database import get_session
from src.infra.repositories.exceptions import link_exception
from src.infra.repositories.models.link_model import LinkORM
from uuid import UUID
from typing import List
from sqlalchemy import exists
import sqlalchemy.exc
from src.logger import error_logger

class LinkRepositoryImpl(LinkRepository):
	def create(self, link: Link) -> Link:
		try:
			with get_session() as session:
				exists_query = session.query(
					exists().where(
						(LinkORM.owner_id == link.owner_id),
						(LinkORM.original_url == str(link.original_url)),
					)
				).scalar()
				if exists_query:
					raise link_exception.InfraLinkAlreadyExists()
				new_link = LinkORM(
					original_url=str(link.original_url),
					short_code=link.short_code,
					owner_id=link.owner_id,
					alias=link.alias,
					room_id=link.room_id
				)
				session.add(new_link)
				session.commit()
				session.refresh(new_link)
				return Link.from_orm(new_link)
		except link_exception.InfraLinkAlreadyExists as e:
			raise e
		except Exception as e:
				error_logger.error(f"{str(e)}", exc_info=True)
				raise link_exception.InfraInvalidCreateLink()

	def check_short_code(self, short_code: str) -> bool:
		try:
			with get_session() as session:
				return session.query(
					exists().where(LinkORM.short_code == short_code)
				).scalar()
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise link_exception.InfraInvalidCheckShortCode() from e

	def get_by_short_code(self, short_code: str) -> Link:
		try:
			with get_session() as session:
				link = session.query(LinkORM).filter(LinkORM.short_code == short_code).first()
				if not link:
					raise link_exception.InfraLinkNotExists()
				return Link.from_orm(link)
		except link_exception.InfraLinkNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise link_exception.InfraInvalidGetLink() from e

	def get_by_alias(self, alias: str, owner_id: UUID = None) -> Link:
		try:
			with get_session() as session:
				query = session.query(LinkORM).filter(LinkORM.alias == alias)
				if owner_id is not None:
					query = query.filter(LinkORM.owner_id == owner_id)
				link = query.first()
				if not link:
					raise link_exception.InfraLinkNotExists()
				return Link.from_orm(link)
		except link_exception.InfraLinkNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise link_exception.InfraInvalidGetLink() from e

	def get_all_by_owner_id(self, owner_id: UUID) -> List[Link]:
		try:
			with get_session() as session:
				links = session.query(LinkORM).filter(LinkORM.owner_id == owner_id).all()
				if not links:
					raise link_exception.InfraLinksNotExist()
				return [Link.from_orm(link) for link in links]
		except link_exception.InfraLinksNotExist as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise link_exception.InfraInvalidGetAllLinks() from e

	def delete_link_by_owner_id_by_link_short_code(self, short_code: str, owner_id: UUID) -> bool:
		try:
			with get_session() as session:
				query = session.query(LinkORM).filter(LinkORM.owner_id == owner_id,
				                                      LinkORM.short_code == short_code).first()
				if not query:
					raise link_exception.InfraLinkNotExists()
				session.delete(query)
				session.commit()
				return True
		except link_exception.InfraLinkNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise link_exception.InfraInvalidDeleteLink() from e

	def delete_link_by_owner_id_by_alias(self, alias: str, owner_id: UUID) -> bool:
		try:
			with get_session() as session:
				query = session.query(LinkORM).filter(LinkORM.owner_id == owner_id,
				                                      LinkORM.alias == alias).first()
				if not query:
					raise link_exception.InfraLinkNotExists()
				session.delete(query)
				session.commit()
				return True
		except link_exception.InfraLinkNotExists as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise link_exception.InfraInvalidDeleteLink() from e

	def delete_all_by_owner_id(self, owner_id: UUID) -> bool:
		try:
			with get_session() as session:
				query = session.query(LinkORM).filter(LinkORM.owner_id == owner_id).delete(synchronize_session=False)
				if query == 0:
					raise link_exception.InfraLinksNotExist()
				session.commit()
				return True
		except link_exception.InfraLinksNotExist as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise link_exception.InfraInvalidDeleteAllLinks() from e