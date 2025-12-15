import re
from jose import jwt, JWTError, ExpiredSignatureError
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request as StarletteRequest
from starlette.responses import JSONResponse
from starlette.status import HTTP_401_UNAUTHORIZED
from starlette.types import ASGIApp
from settings import config as cg
from src.logger import status_logger

PROTECTED_PATHS = ["/user/create-link",
                   "/user/change-password",
                   "/user/change-username",
                   "/user/change-email",
                   "/user/change-name",
                   "/user/my-links",
                   "/user/link/{link_id}",
                   "/user/links",
                   "/user/"
                   ]


class JWTMiddleware(BaseHTTPMiddleware):
	def __init__(self, app: ASGIApp):
		super().__init__(app)
		# Преобразуем паттерны в регулярные выражения один раз при инициализации
		self.protected_path_patterns = [
			re.compile(
				"^" + re.sub(r"\{[^/]+\}", r"[^/]+", path) + "$"
			)
			for path in PROTECTED_PATHS
		]

	def is_protected_path(self, path: str) -> bool:
		for pattern in self.protected_path_patterns:
			if pattern.match(path):
				return True
		return False

	@staticmethod
	def decode_token(token: str):
		try:
			payload = jwt.decode(token, cg.ACCESS_SECRET, algorithms=["HS256"])
			return payload
		except ExpiredSignatureError:
			# ⛔ токен истёк
			return None
		except JWTError:
			return None

	async def dispatch(self, request: StarletteRequest, call_next):
		path = request.url.path
		auth_header = request.headers.get("Authorization", "")
		token = None

		if auth_header.startswith("Bearer "):
			token = auth_header.replace("Bearer ", "")

		if token:
			payload = self.decode_token(token)
			if (
					payload
					and payload.get("type") == "access"
					and "sub" in payload
					and "username" in payload
			):
				request.state.user_id = payload["sub"]
				request.state.username = payload["username"]
				
			elif self.is_protected_path(path):
				status_logger.info(f"Invalid or expired token for path: {path}")
				return JSONResponse(status_code=HTTP_401_UNAUTHORIZED, content={"detail": "Invalid or expired token"})

		elif self.is_protected_path(path):
			status_logger.info(f"Authorization token missing for path: {path}")
			return JSONResponse(status_code=HTTP_401_UNAUTHORIZED, content={"detail": "Authorization token missing"})

		return await call_next(request)