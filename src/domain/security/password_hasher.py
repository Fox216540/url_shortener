from abc import ABC, abstractmethod


class PasswordHasher(ABC):
	@abstractmethod
	def hash(self, plain: str) -> str:
		pass

	@abstractmethod
	def verify(self, plain: str, hashed: str) -> bool:
		pass
