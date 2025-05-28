# app/di.py
from src.infra.repositories.link_repo import LinkRepositoryImpl
from src.app.service.link_service import LinkService


def get_service() -> LinkService:
    repo = LinkRepositoryImpl()
    return LinkService(repo)
