# app/di.py
from src.infra.repositories.link_repo import LinkRepositoryImpl
from src.app.service.link_service import LinkService
from src.infra.repositories.user_repo import UserRepositoryImpl
from src.app.service.user_service import UserService
from src.infra.security.passlib_hasher import PasslibHasher


def get_link_service() -> LinkService:
    repo = LinkRepositoryImpl()
    return LinkService(repo)


def get_user_service() -> UserService:
    repo = UserRepositoryImpl()
    hasher = PasslibHasher()
    link_service = get_link_service()
    return UserService(repo, hasher, link_service)

