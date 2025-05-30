import base62
from typing import Optional
from src.domain.link.models.link import Link
from src.domain.link.repositories.link_repo import LinkRepository
from src.domain.user.repositories.user_repo import UserRepository
from uuid import UUID


class LinkService:
	def __init__(self, repo: LinkRepository, user: UserRepository):
		self.repo = repo
		self.user = user

	def add_link(self, url: str, owner_id: UUID = None, alias: str = None) -> Optional[Link]:
		link = Link(original_url=url, owner_id=owner_id, alias=alias)
		return self.repo.create(link)

	def get_url_by_short_code(self, identifier: str, username: str = None) -> Optional[Link]:
		user = self.user.get_by_username(username)
		try:
			link_id = base62.decode(identifier)
			link = self.repo.get_by_id(link_id, user.id if user else None)
			if link:
				return link
		except ValueError:
			pass
		return self.repo.get_by_alias(identifier, user.id if user else None)
