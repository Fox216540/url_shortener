import base62
from typing import Optional
from src.domain.link.models.link import Link
from src.domain.link.repositories.link_repo import LinkRepository
from uuid import UUID


class LinkService:
	def __init__(self, repo: LinkRepository):
		self.repo = repo

	def add_link(self, url: str, owner_id: UUID = None) -> Optional[str]:
		link = Link(original_url=url, owner_id=owner_id)
		saved = self.repo.create(link)
		return saved.short_code

	def get_url_by_short_code(self, short_code: str) -> Optional[str]:
		try:
			link_id = base62.decode(short_code)     # декодируем строку в int
		except ValueError:
			return None  # неверный формат short_code
		link = self.repo.get_by_id(link_id)  # запрашиваем по int-ID
		return link.original_url
