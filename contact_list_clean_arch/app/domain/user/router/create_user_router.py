import logging

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from contact_list_clean_arch.app.config.bean import get_create_user_use_case
from contact_list_clean_arch.app.domain.user.use_case.create_user_use_case import InputModel

router = APIRouter()
logger = logging.getLogger(__name__)


class Request(BaseModel):
    name: str
    email: str
    password: str


class Response:
    user_id: str

    def __init__(self, user_id: str):
        self.user_id = user_id


@router.post("/users", status_code=201, )
def create_user(request: Request, use_case=Depends(get_create_user_use_case)) -> Response:

    input_model = InputModel(name=request.name, email=request.email, password=request.password)

    output = use_case.execute(input_model)

    return Response(output.user_id)
