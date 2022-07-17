import logging

from fastapi import APIRouter, Depends

from contact_list_clean_arch.app.domain.auth.middleware.authorization_meddleware import JWTBearerMiddleware
from contact_list_clean_arch.app.config.bean import get_create_contact_use_case
from pydantic import BaseModel
from contact_list_clean_arch.app.domain.contact.model.contact import Contact
from contact_list_clean_arch.app.domain.contact.use_case.create_contact_use_case import InputModel

router = APIRouter()
logger = logging.getLogger(__name__)


class Request(BaseModel):
    name: str
    phone: str


class Response:
    contact_id: int

    def __init__(self, contact_id: int):
        self.contact_id = contact_id


@router.post("/users/{user_id}/contacts",
             status_code=201,
             dependencies=[Depends(JWTBearerMiddleware())])
def create_contact(user_id: str, request: Request, use_case=Depends(get_create_contact_use_case)) -> Response:
    logger.info("M=create_contact")

    contact = Contact(name=request.name, phone=request.phone, user_id=user_id)
    input_model = InputModel(contact=contact)

    output_model = use_case.execute(input_model)

    return Response(output_model.contact.contact_id)
