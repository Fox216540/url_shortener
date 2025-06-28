import secrets
import string
from typing import List
from uuid import UUID
from src.domain.link.models.link import Link
from src.domain.link.repositories.link_repo import LinkRepository
from src.domain.link.exceptions.link_exceptions import LinkException
from src.app.exceptions.link_exceptions import (
	InvalidAddLink, InvalidGetUrlByShortCode, InvalidGetAllLinksByOwnerId,
	InvalidDeleteLinkByOwnerId, InvalidDeleteAllByOwnerId,
)

class LinkService:
	def __init__(self, repo: LinkRepository):
		self._repo = repo

	@staticmethod
	def _generate_short_code(length=8):
		alphabet = string.ascii_letters + string.digits
		return ''.join(secrets.choice(alphabet) for _ in range(length))

	def add_link(self, url: str, owner_id: UUID = None, alias: str = None, room_id: UUID = None) -> Link:
		try:
			max_attempts = 10
			for _ in range(max_attempts):
				short_code = self._generate_short_code()
				if self._repo.check_short_code(short_code):
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
			raise InvalidAddLink() from e

	def get_url_by_short_code(self, identifier: str, owner_id: UUID = None) -> Link:
		try:
			link = self._repo.get_by_alias(identifier, owner_id)
			if not link:
				link = self._repo.get_by_short_code(identifier)
			return link
		except LinkException as e:
			raise e
		except Exception as e:
			raise InvalidGetUrlByShortCode() from e

	def get_all_links_by_owner_id(self, owner_id: UUID) -> List[Link]:
		try:
			return self._repo.get_all_by_owner_id(owner_id)
		except LinkException as e:
			raise e
		except Exception as e:
			raise InvalidGetAllLinksByOwnerId() from e

	def delete_link_by_owner_id(self, identifier: str, owner_id: UUID) -> bool:
		try:
			link = self._repo.delete_link_by_owner_id_by_alias(identifier, owner_id)
			if not link:
				link = self._repo.delete_link_by_owner_id_by_link_short_code(identifier, owner_id)
			return link
		except LinkException as e:
			raise e
		except Exception as e:
			raise InvalidDeleteLinkByOwnerId() from e

	def delete_all_by_owner_id(self, owner_id: UUID) -> bool:
		try:
			return self._repo.delete_all_by_owner_id(owner_id)
		except LinkException as e:
			raise e
		except Exception as e:
			raise InvalidDeleteAllByOwnerId() from e
