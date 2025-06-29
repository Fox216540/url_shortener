from src.domain.health.health import Health
from src.infra.database import get_session
from src.infra.redis_conn import get_redis
from src.logger import error_logger
from src.infra.health.exceptions.health_exceptions import (
	InfraInvalidDbConnection, InfraInvalidTSConnection
)
class HealthImpl(Health):
	def check_health_db(self) -> bool:
		try:
			with get_session() as session:
				session.execute(session.query(1).statement)
				return True
		except Exception as e:
			error_logger.error(f"Database connection failed: {str(e)}", exc_info=True)
			raise InfraInvalidDbConnection() from e

	def check_health_token_storage(self) -> bool:
		try:
			with get_redis() as client:
				client.ping()
				return True
		except Exception as e:
			error_logger.error(f"Redis connection failed: {str(e)}", exc_info=True)
			raise InfraInvalidTSConnection() from e