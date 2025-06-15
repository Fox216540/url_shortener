import secrets
import string
from typing import Optional
from src.domain.link.models.link import Link
from src.domain.link.repositories.link_repo import LinkRepository
from uuid import UUID

from src.infra.repositories.exceptions.link import InvalidCreateLink
from typing import List


class LinkService:
	def __init__(self, repo: LinkRepository):
		self._repo = repo

	@staticmethod
	def _generate_short_code(length=8):
		alphabet = string.ascii_letters + string.digits
		return ''.join(secrets.choice(alphabet) for _ in range(length))

	def add_link(self, url: str, owner_id: UUID = None, alias: str = None, room_id: UUID = None) -> Optional[Link]:
		max_attempts = 10
		short_code = None
		for _ in range(max_attempts):
			short_code = self._generate_short_code()
			if not self._repo.check_short_code(short_code):
				break
		else:
			pass
		link = Link(
			original_url=url,
			owner_id=owner_id,
			alias=alias,
			short_code=short_code,
			room_id=room_id
		)
		try:
			return self._repo.create(link)
		except InvalidCreateLink as e:
			raise e

	def get_url_by_short_code(self, identifier: str, owner_id: UUID = None) -> Optional[Link]:
		link = self._repo.get_by_alias(identifier, owner_id)
		if not link:
			link = self._repo.get_by_short_code(identifier)
		return link

	def get_all_links_by_owner_id(self, owner_id: UUID) -> Optional[List[Link]]:
		return self._repo.get_all_by_owner_id(owner_id)

	def delete_link_by_owner_id(self, identifier: str, owner_id: UUID) -> Optional[bool]:
		link = self._repo.delete_link_by_owner_id_by_alias(identifier, owner_id)
		if not link:
			link = self._repo.delete_link_by_owner_id_by_link_short_code(identifier, owner_id)
		return link

	def delete_all_by_owner_id(self, owner_id: UUID) -> Optional[bool]:
		return self._repo.delete_all_by_owner_id(owner_id)
