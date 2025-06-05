from jose import jwt
from datetime import datetime, timedelta
from src.domain.security.jwt import JWT
from uuid import UUID
from uuid import uuid4 as uuid4
from settings import ACCESS_TOKEN_TIME, REFRESH_TOKEN_TIME


class JWTImpl(JWT):
    def __init__(self, secret: str):
        self.secret = secret

    def create_access_token(self, user_id: UUID, username: str) -> str:
        payload = {"sub": str(user_id),
                   "type": "access",
                   "username": username,
                   "exp": datetime.utcnow() + timedelta(seconds=ACCESS_TOKEN_TIME)}
        return jwt.encode(payload, self.secret, algorithm="HS256")

    def create_refresh_token(self, user_id: UUID) -> tuple:
        jti = str(uuid4)
        payload = {"sub": str(user_id),
                   "jti": jti,
                   "type": "refresh",
                   "exp": datetime.utcnow() + timedelta(seconds=REFRESH_TOKEN_TIME)}
        return jwt.encode(payload, self.secret, algorithm="HS256"), jti

    def decode(self, token: str) -> dict:
        return jwt.decode(token, self.secret, algorithms=["HS256"])
