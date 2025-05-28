import base62
from typing import Optional
from src.domain.link.models.link import Link
from src.domain.link.repositories.link_repo import LinkRepository
from uuid import UUID


class LinkService:
	def __init__(self, repo: LinkRepository):
		self.repo = repo

	def add_link(self, url: str, owner_id: UUID = None, alias: str = None) -> Optional[Link]:
		link = Link(original_url=url, owner_id=owner_id, alias=alias)
		saved = self.repo.create(link)
		if alias:
			return saved.alias
		return saved

	def get_url_by_short_code(self, identifier: str) -> Optional[Link]:
		try:
			link_id = base62.decode(identifier)
			link = self.repo.get_by_id(link_id)
			if link:
				return link
		except ValueError:
			pass

		# Если не base62 или не найдено по ID - ищем по alias
		return self.repo.get_by_alias(identifier)
