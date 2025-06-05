# app/di.py
from src.infra.repositories.link_repo import LinkRepositoryImpl
from src.app.service.link_service import LinkService
from src.infra.repositories.user_repo import UserRepositoryImpl
from src.app.service.user_service import UserService
from src.app.service.auth_service import AuthService
from src.infra.security.passlib_hasher import PasslibHasher
from src.infra.security.jwt_impl import JWTImpl
from src.infra.security.token_storage_impl import TokenStorageImpl
from settings import ACCESS_SECRET


def get_link_service() -> LinkService:
	repo = LinkRepositoryImpl()
	user = UserRepositoryImpl()
	return LinkService(repo, user)


def get_auth_service() -> AuthService:
	jwt = JWTImpl(ACCESS_SECRET)
	token_storage = TokenStorageImpl()
	return AuthService(jwt, token_storage)


def get_user_service() -> UserService:
	repo = UserRepositoryImpl()
	hasher = PasslibHasher()
	link_service = get_link_service()
	auth_service = get_auth_service()
	return UserService(repo, hasher, link_service, auth_service)

