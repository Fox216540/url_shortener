from dataclasses import dataclass
from src.domain.user.models.user import User  # твоя сущность


@dataclass
class UserResult:
    user: User
    access_token: str
    refresh_token: str
