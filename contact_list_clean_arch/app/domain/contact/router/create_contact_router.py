import logging

from fastapi import APIRouter, Depends

from contact_list_clean_arch.app.domain.auth.middleware.authorization_meddleware import JWTBearerMiddleware
from pydantic import BaseModel
from contact_list_clean_arch.app.domain.contact.model.contact import Contact
from contact_list_clean_arch.app.domain.contact.use_case.create_contact_use_case import InputModel, CreateContactUseCase
from contact_list_clean_arch.app.domain.user.gateway.db.user_in_memory_gateway import UserInMemoryGateway

router = APIRouter()
logger = logging.getLogger(__name__)


class Request(BaseModel):
    name: str
    phone: str


class Response:
    contact_id: str

    def __init__(self, contact_id: str):
        self.contact_id = contact_id


@router.post("/users/{user_id}/contacts",
             status_code=201,
             dependencies=[Depends(JWTBearerMiddleware())])
def create_contact(user_id: str, request: Request,
                   use_case: CreateContactUseCase = Depends(CreateContactUseCase)) -> Response:
    logger.info("M=create_contact")

    contact = Contact(name=request.name, phone=request.phone, user_id=user_id)
    input_model = InputModel(contact=contact)

    output_model = use_case.execute(input_model)

    return Response(output_model.contact.contact_id)
