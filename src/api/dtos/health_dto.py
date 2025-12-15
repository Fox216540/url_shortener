from pydantic import BaseModel

	
class HealthResponse(BaseModel):
	status: str = "ok"

class HealthDbResponse(HealthResponse):
	db_status: str = "ok"

class HealthTokenStorageResponse(HealthResponse):
	token_status: str = "ok"
	
class HealthAllStatus(HealthDbResponse):
	token_status: str = "ok"