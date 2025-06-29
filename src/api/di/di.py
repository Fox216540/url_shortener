from settings import ACCESS_SECRET
from src.infra.repositories.link_repo import LinkRepositoryImpl
from src.app.service.link_service import LinkService
from src.infra.repositories.user_repo import UserRepositoryImpl
from src.app.service.user_service import UserService
from src.app.service.mesage_service import MessageService
from src.infra.repositories.message_repo import MessageRepositoryImpl
from src.app.service.auth_service import AuthService
from src.infra.security.passlib_hasher_impl import PasslibHasher
from src.infra.security.jwt_impl import JWTImpl
from src.infra.security.token_storage_impl import TokenStorageImpl
from src.infra.websocket.connection_manager import ConnectionManager
from src.app.service.websocket_service import WebsocketService
from src.app.service.health_service import HealthService
from src.infra.health.health_impl import HealthImpl
from src.api.exceptions.error import Error


def get_link_service() -> LinkService:
	repo = LinkRepositoryImpl()
	return LinkService(repo)

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


def get_message_service() -> MessageService:
	repo = MessageRepositoryImpl()
	user_service = get_user_service()
	return MessageService(repo, user_service)


_connection_manager = ConnectionManager()
_websocket_service = WebsocketService(connect=_connection_manager)


def get_connection_manager() -> WebsocketService:
	return _websocket_service

def get_error() -> Error:
	error = Error()
	return error

def get_health_service() -> HealthService:
	health = HealthImpl()
	return HealthService(health)
