import logging

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from contact_list_clean_arch.app.use_case.auth.user_authentication_use_case import UserAuthenticationUseCase, InputModel

router = APIRouter()
logger = logging.getLogger(__name__)


class Request(BaseModel):
    email: str
    password: str


class Response(BaseModel):
    authorization_token: str


@router.post("/login", status_code=200)
def create_user(request: Request, use_case: UserAuthenticationUseCase = Depends(UserAuthenticationUseCase)) -> Response:

    input_model = InputModel(email=request.email, password=request.password)

    output = use_case.execute(input_model)

    return Response(authorization_token=output.authorization_token)
