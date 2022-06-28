import logging

from fastapi import APIRouter, Depends

from contact_list_clean_arch.app.config.exception_handler import with_exception_handler
from pydantic import BaseModel
from contact_list_clean_arch.app.contact.model.contact import Contact
from contact_list_clean_arch.app.contact.use_case.create_contact_use_case import InputModel, CreateContactUseCase

router = APIRouter()
logger = logging.getLogger(__name__)


class Request(BaseModel):
    name: str
    phone: str


class Response:
    contact_id: int

    def __init__(self, contact_id: int):
        self.contact_id = contact_id


@router.post("/contacts", status_code=201)
def create_contact(request: Request, use_case=Depends(CreateContactUseCase)) -> Response:
    logger.info("M=create_contact")

    contact = Contact(name=request.name, phone=request.phone)
    input_model = InputModel(contact)

    output_model = with_exception_handler(lambda: use_case.execute(input_model))

    return Response(output_model.contact.contact_id)
