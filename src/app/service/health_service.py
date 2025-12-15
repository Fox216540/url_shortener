from src.domain.health.health import Health
from src.domain.health.exceptions.health_exceptions import (
	InvalidDbConnection, HealthException, InvalidTSConnection
)
from src.app.exceptions.health_exceptions import (
	InvalidGetDbHealthStatus, InvalidGetTsHealthStatus, InvalidGetAllHealthStatus
)
from src.domain.health.exceptions.health_exceptions import InvalidAllConnection
from src.logger import error_logger


class HealthService:
	def __init__(self, health: Health):
		self._health = health

	def check_all_health_status(self) -> bool:
		try:
			db_ok = self._health.check_health_db()
		except InvalidDbConnection as db_exc:
			try:
				self._health.check_health_token_storage()
			except InvalidTSConnection:
				raise InvalidAllConnection() from db_exc
			else:
				raise db_exc
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidGetAllHealthStatus()
		else:
			try:
				ts_ok = self._health.check_health_token_storage()
			except InvalidTSConnection as ts_exc:
				raise ts_exc
		return db_ok and ts_ok
		
	def check_db_health_status(self) -> bool:
		try:
			return self._health.check_health_db()
		except HealthException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidGetDbHealthStatus()

	def check_ts_health_status(self) -> bool:
		try:
			return self._health.check_health_token_storage()
		except HealthException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidGetTsHealthStatus()

