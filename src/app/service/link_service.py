import secrets
import string
from typing import List
from pydantic import HttpUrl
from uuid import UUID
from src.domain.link.models.link import Link
from src.domain.link.repositories.link_repo import LinkRepository
from src.domain.link.exceptions.link_exceptions import LinkException, LinkNotFoundException
from src.app.exceptions.link_exceptions import (
	LinkServiceException,
	InvalidAddLink, InvalidGetUrlByShortCode, InvalidGetAllLinksByOwnerId,
	InvalidDeleteLinkByOwnerId, InvalidDeleteAllByOwnerId,
)
from src.logger import error_logger


class LinkService:
	def __init__(self, repo: LinkRepository):
		self._repo = repo

	@staticmethod
	def _generate_short_code(length=8):
		alphabet = string.ascii_letters + string.digits
		return ''.join(secrets.choice(alphabet) for _ in range(length))

	def add_link(self, url: HttpUrl, owner_id: UUID = None, alias: str = None, room_id: UUID = None) -> Link:
		try:
			max_attempts = 10
			for _ in range(max_attempts):
				short_code = self._generate_short_code()
				if not self._repo.check_short_code(short_code):
					break
			else:
				raise InvalidAddLink()
			link = Link(
				original_url=url,
				owner_id=owner_id,
				alias=alias,
				short_code=short_code,
				room_id=room_id
			)
			return self._repo.create(link)
		except (LinkException, InvalidAddLink) as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidAddLink() from e

	def get_url_by_short_code_or_alias(self, identifier: str, owner_id: UUID = None) -> Link:
		try:
			try:
				return self._get_url_by_alias(identifier, owner_id)
			except LinkNotFoundException:
				return self._get_url_by_short_code(identifier)
		except (LinkServiceException, LinkException) as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidGetUrlByShortCode() from e

	def _get_url_by_alias(self, alias: str, owner_id: UUID = None) -> Link:
		try:
			return self._repo.get_by_alias(alias, owner_id)
		except LinkException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidGetUrlByShortCode() from e

	def _get_url_by_short_code(self, short_code: str) -> Link:
		try:
			return self._repo.get_by_short_code(short_code)
		except LinkException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidGetUrlByShortCode() from e

	def get_all_links_by_owner_id(self, owner_id: UUID) -> List[Link]:
		try:
			return self._repo.get_all_by_owner_id(owner_id)
		except LinkException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidGetAllLinksByOwnerId() from e

	def delete_link_by_owner_id(self, identifier: str, owner_id: UUID) -> bool:
		try:
			try:
				return self._delete_link_by_owner_id_by_alias(identifier, owner_id)
			except LinkNotFoundException:
				return self._delete_link_by_owner_id_by_short_code(identifier, owner_id)
		except (LinkServiceException, LinkException) as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidDeleteLinkByOwnerId() from e

	def _delete_link_by_owner_id_by_alias(self, alias: str, owner_id: UUID) -> bool:
		try:
			return self._repo.delete_link_by_owner_id_by_alias(alias, owner_id)
		except LinkException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidDeleteLinkByOwnerId() from e

	def _delete_link_by_owner_id_by_short_code(self, short_code: str, owner_id: UUID) -> bool:
		try:
			return self._repo.delete_link_by_owner_id_by_link_short_code(short_code, owner_id)
		except LinkException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidDeleteLinkByOwnerId() from e

	def delete_all_by_owner_id(self, owner_id: UUID) -> bool:
		try:
			return self._repo.delete_all_by_owner_id(owner_id)
		except LinkException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidDeleteAllByOwnerId() from e
