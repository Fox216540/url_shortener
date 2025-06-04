from jose import jwt
from datetime import datetime, timedelta
from src.domain.security.jwt import JWT
from uuid import UUID


class JWTImpl(JWT):
    def __init__(self, secret: str):
        self.secret = secret

    def create_access_token(self, user_id: UUID, username: str) -> str:
        payload = {"sub": str(user_id), "username": username, "exp": datetime.utcnow() + timedelta(days=7)}
        return jwt.encode(payload, self.secret, algorithm="HS256")

    def create_refresh_token(self, user_id: UUID) -> str:
        payload = {"sub": str(user_id), "exp": datetime.utcnow() + timedelta(days=7)}
        return jwt.encode(payload, self.secret, algorithm="HS256")

    def decode(self, token: str) -> dict:
        return jwt.decode(token, self.secret, algorithms=["HS256"])
