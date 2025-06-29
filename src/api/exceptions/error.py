from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_503_SERVICE_UNAVAILABLE
from src.domain.link.exceptions.link_exceptions import LinkNotFoundException
from src.domain.user.exceptions.user_exceptions import UserNotFoundException
from src.domain.message.exceptions.message_exceptions import MessageNotFoundException
from src.domain.security.exceptions.token_storage_exception import TokenStorageNotFoundException
from src.app.exceptions.user_exceptions import UserDataException
from src.api.exceptions.error_messages import BadRequestErrorMessage, InternalServerErrorMessage
from src.api.exceptions.health_exceptions import NameOfHealthNotExist
from src.api.exceptions.message_exceptions import MessageHandlerException
from src.domain.health.exceptions.health_exceptions import HealthException
from src.logger import status_logger

class Error:
	def handle(
			self,
			exc: Exception,
			details: dict = None,
	) -> HTTPException:
		status_logger.info(f"Error occurred: \n{exc}")
		
		if isinstance(exc, (
				LinkNotFoundException, UserNotFoundException,
				MessageNotFoundException, TokenStorageNotFoundException,
				UserDataException, MessageHandlerException, NameOfHealthNotExist
		)):
			raise HTTPException(
				status_code=HTTP_400_BAD_REQUEST,
				detail=BadRequestErrorMessage
			)
		
		if isinstance(exc, HealthException):
			raise HTTPException(
				status_code=HTTP_503_SERVICE_UNAVAILABLE,
			    detail=details
			)
		
		raise HTTPException(
			status_code=HTTP_500_INTERNAL_SERVER_ERROR,
			detail=InternalServerErrorMessage
		)
