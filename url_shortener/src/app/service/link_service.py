import base62
from typing import Optional
from url_shortener.src.infra.repositories.link_repo import LinkRepositoryImpl
from url_shortener.src.domain.link.models.link import Link


class LinkService:
	def __init__(self, repo: LinkRepositoryImpl):
		self.repo = repo

	def add_link(self, url: str) -> Optional[str]:
		link = Link(original_url=url)
		saved = self.repo.add(link)
		return saved.short_code

	def get_url_by_short_code(self, short_code: str) -> Optional[str]:
		try:
			link_id = base62.decode(short_code)     # декодируем строку в int
		except ValueError:
			return None  # неверный формат short_code
		link = self.repo.get_by_id(link_id)     # запрашиваем по int-ID
		return link.original_url
