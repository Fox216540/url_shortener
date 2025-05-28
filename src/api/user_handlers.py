from fastapi import APIRouter

from src.app.service.user_service import UserService
from src.app.dtos.user_dto import (CreateUserResponse,
                                   CreateUserRequest,
                                   GetUuidOfUserRequest,
                                   GetUuidOfUserResponse)
from fastapi import Depends

from src.app.di.di import get_user_service
from src.domain.user.models.user import User

#from app.logger import logger

router = APIRouter(tags=["User"])


@router.post("/user", response_model=GetUuidOfUserResponse)
def get_uuid_of_user(request: GetUuidOfUserRequest, service: UserService = Depends(get_user_service)):
    uuid = service.get_id_by_mail_password(mail=request.mail, password=request.password)
    return GetUuidOfUserResponse(uuid=uuid)


@router.post("/reg", response_model=CreateUserResponse)
def create_user(request: CreateUserRequest, service: UserService = Depends(get_user_service)):
    user = User(**request.dict())
    status_message = service.create_user(user)
    return CreateUserResponse(message=status_message)


