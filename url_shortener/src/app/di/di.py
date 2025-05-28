# app/di.py
from url_shortener.src.infra.repositories.link_repo import LinkRepositoryImpl
from url_shortener.src.app.service.link_service import LinkService


def get_service() -> LinkService:
    repo = LinkRepositoryImpl()
    return LinkService(repo)
