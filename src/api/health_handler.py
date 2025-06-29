from fastapi import APIRouter, Depends
from src.api.exceptions.health_exceptions import NameOfHealthNotExist
from src.api.di.di import get_health_service, get_error
from src.api.dtos.health_dto import HealthAllStatus
from src.app.service.health_service import HealthService
from src.domain.health.exceptions.health_exceptions import (
	InvalidDbConnection, InvalidTSConnection, InvalidAllConnection
)
from src.api.dtos.health_dto import HealthDbResponse, HealthTokenStorageResponse, HealthResponse
from src.api.exceptions.error import Error

router = APIRouter(tags=["health"])

@router.get("/live", response_model=HealthResponse)
def get_live_status():
	return HealthResponse()

@router.get("/health", response_model=HealthAllStatus)
def get_all_status(
    health_service: HealthService = Depends(get_health_service),
    error: Error = Depends(get_error)
):
	all_status = HealthAllStatus()
	try:
		health_service.get_all_health_status()
		return all_status
	except InvalidTSConnection as e:
		all_status.status = "error"
		all_status.token_status = "unreachable"
		return error.handle(e, all_status.model_dump())
	except InvalidDbConnection as e:
		all_status.status = "error"
		all_status.db_status = "unreachable"
		return error.handle(e, all_status.model_dump())
	except InvalidAllConnection as e:
		all_status.status = "error"
		all_status.db_status = "unreachable"
		all_status.token_status = "unreachable"
		return error.handle(e, all_status.model_dump())
	except Exception as e:
		return error.handle(e)

@router.get("/health/{project_object}")
def get_status_of_project_object(
	project_object: str,
    health_service: HealthService = Depends(get_health_service),
    error: Error = Depends(get_error),
):
	try:
		if project_object == "db":
			health_service.get_db_health_status()
			return HealthDbResponse()
		elif project_object == "token":
			health_service.get_ts_health_status()
			return HealthTokenStorageResponse()
		else:
			raise NameOfHealthNotExist()
	except InvalidTSConnection as e:
		status = HealthTokenStorageResponse()
		status.status = "error"
		status.token_status = "unreachable"
		return error.handle(e, status.model_dump())
	except InvalidDbConnection as e:
		status = HealthDbResponse()
		status.status = "error"
		status.db_status = "unreachable"
		return error.handle(e, status.model_dump())
	except Exception as e:
		return error.handle(e)

