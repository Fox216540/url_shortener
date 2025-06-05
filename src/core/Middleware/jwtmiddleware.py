from fastapi import HTTPException
from jose import jwt, JWTError, ExpiredSignatureError
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request as StarletteRequest
from starlette.types import ASGIApp
from settings import ACCESS_SECRET

PROTECTED_PATHS = ["/user/create-link",
                   "/user/change-password",
                   "/user/change-username",
                   "/user/change-email",
                   "/user/change-name",
                   "/user/my-links",
                   "/user/link/",
                   "/user/links"
                   ]  # пути, к которым применяется авторизация "/reg",


class JWTMiddleware(BaseHTTPMiddleware):
	def __init__(self, app: ASGIApp):
		super().__init__(app)

	@staticmethod
	def is_protected_path(path: str) -> bool:
		return any(path.startswith(p) for p in PROTECTED_PATHS)

	@staticmethod
	def decode_token(token: str):
		try:
			payload = jwt.decode(token, ACCESS_SECRET, algorithms=["HS256"])
			return payload
		except ExpiredSignatureError:
			# ⛔ токен истёк
			return None
		except JWTError:
			return None

	async def dispatch(self, request: StarletteRequest, call_next):
		path = request.url.path

		if self.is_protected_path(path):
			auth_header = request.headers.get("Authorization", "")
			if auth_header.startswith("Bearer "):
				token = auth_header.replace("Bearer ", "")
				payload = self.decode_token(token)
				if (
					not payload
					or payload.get("type") != "access"
					or "sub" not in payload
					or "username" not in payload
				):
					raise HTTPException(status_code=401, detail="Invalid or expired token")
				request.state.user_id = payload["sub"]
				request.state.username = payload["username"]
			else:
				raise HTTPException(status_code=401, detail="Authorization token missing")

		return await call_next(request)
