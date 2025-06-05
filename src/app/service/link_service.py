import base62
from typing import Optional
from src.domain.link.models.link import Link
from src.domain.link.repositories.link_repo import LinkRepository
from uuid import UUID
from typing import List


class LinkService:
	def __init__(self, repo: LinkRepository):
		self._repo = repo

	def add_link(self, url: str, owner_id: UUID = None, alias: str = None) -> Optional[Link]:
		link = Link(original_url=url, owner_id=owner_id, alias=alias)
		return self._repo.create(link)

	def get_url_by_short_code(self, identifier: str, owner_id: UUID = None) -> Optional[Link]:
		try:
			link_id = base62.decode(identifier)
			link = self._repo.get_by_id(link_id, owner_id if owner_id else None)
			return link
		except ValueError:
			pass
		return self._repo.get_by_alias(identifier, owner_id if owner_id else None)

	def get_all_links_by_owner_id(self, owner_id: UUID) -> Optional[List[Link]]:
		links = self._repo.get_all_by_owner_id(owner_id)
		return links

	def delete_link_by_owner_id(self, identifier: str, owner_id: UUID) -> Optional[bool]:
		try:
			link_id = base62.decode(identifier)
			link_status = self._repo.delete_link_by_owner_id_by_link_id(link_id, owner_id)
			return link_status
		except ValueError:
			pass
		return self._repo.delete_link_by_owner_id_by_alias(identifier, owner_id)

	def delete_all_by_owner_id(self, owner_id: UUID) -> Optional[bool]:
		return self._repo.delete_all_by_owner_id(owner_id)
