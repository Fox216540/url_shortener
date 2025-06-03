import base62
from typing import Optional
from src.domain.link.models.link import Link
from src.domain.link.repositories.link_repo import LinkRepository
from src.domain.user.repositories.user_repo import UserRepository
from uuid import UUID
from typing import List


class LinkService:
	def __init__(self, repo: LinkRepository, user: UserRepository):
		self._repo = repo
		self._user = user

	def add_link(self, url: str, owner_id: UUID = None, alias: str = None) -> Optional[Link]:
		link = Link(original_url=url, owner_id=owner_id, alias=alias)
		return self._repo.create(link)

	def get_url_by_short_code(self, identifier: str, username: str = None) -> Optional[Link]:
		user = self._user.get_by_username(username)
		try:
			link_id = base62.decode(identifier)
			link = self._repo.get_by_id(link_id, user.id if user else None)
			return link
		except ValueError:
			pass
		return self._repo.get_by_alias(identifier, user.id if user else None)

	def get_all_links_by_user_id(self, user_id: UUID) -> Optional[List[Link]]:
		links = self._repo.get_all_by_owner_id(user_id)
		return links
