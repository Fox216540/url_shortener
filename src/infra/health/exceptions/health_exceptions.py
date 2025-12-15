from src.domain.health.exceptions.health_exceptions import (
	InvalidDbConnection, InvalidTSConnection
)

LAYER = "Infra/health/health"


class InfraInvalidDbConnection(InvalidDbConnection):
	message = "Infra Invalid Database Connection"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraInvalidTSConnection(InvalidTSConnection):
	message = "Infra Invalid Token Storage Connection"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

