import logging

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from contact_list_clean_arch.app.domain.auth.use_case.user_authentication_use_case import InputModel
from contact_list_clean_arch.app.config.bean import get_user_authentication_use_case

router = APIRouter()
logger = logging.getLogger(__name__)


class Request(BaseModel):
    email: str
    password: str


class Response:
    authorization_token: str

    def __init__(self, authorization_token: str):
        self.authorization_token = authorization_token


@router.post("/login", status_code=200)
def create_user(request: Request, use_case=Depends(get_user_authentication_use_case)) -> Response:

    input_model = InputModel(email=request.email, password=request.password)

    output = use_case.execute(input_model)

    return Response(output.authorization_token)
