from jose import jwt
from datetime import datetime, timedelta
from src.domain.security.jwt import JWT
from uuid import UUID
from types import SimpleNamespace

class JWTImpl(JWT):
    def __init__(self, secret: str):
        self.secret = secret

    def create_access_token(self, user_id: UUID, username: str) -> str:
        payload = {"sub": str(user_id), "username": username, "exp": datetime.utcnow() + timedelta(days=7)}
        return jwt.encode(payload, self.secret, algorithm="HS256")

    def create_refresh_token(self, user_id: UUID) -> str:
        payload = {"sub": str(user_id), "exp": datetime.utcnow() + timedelta(days=7)}
        return jwt.encode(payload, self.secret, algorithm="HS256")

    def decode(self, token: str) -> SimpleNamespace:
        token = jwt.decode(token, self.secret, algorithms=["HS256"])
        return SimpleNamespace(**token)

    def refresh(self, refresh_token: str, username: str) -> dict:
        payload = self.decode(refresh_token)
        new_access = self.create_access_token(payload["sub"], username)
        new_refresh = self.create_refresh_token(UUID(payload["sub"]))
        return {"access_token": new_access, "refresh_token": new_refresh}
