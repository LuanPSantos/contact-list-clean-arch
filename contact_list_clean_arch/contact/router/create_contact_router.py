import logging

from fastapi import APIRouter

from contact_list_clean_arch.config.db.db_config import get_session
from contact_list_clean_arch.config.exception_handler import with_exception_handler
from contact_list_clean_arch.contact.gateway.db.contact_command_my_sql_gateway import ContactInMemoryGateway
from pydantic import BaseModel
from contact_list_clean_arch.contact.model.contact import Contact
from contact_list_clean_arch.contact.use_case.create_contact_use_case import CreateContactUseCase, InputModel

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
def create_contact(request: Request) -> Response:
    logger.info("M=create_contact")

    use_case = CreateContactUseCase(ContactInMemoryGateway(get_session))

    contact = Contact(name=request.name, phone=request.phone)
    input_model = InputModel(contact)

    output_model = with_exception_handler(lambda: use_case.execute(input_model))

    return Response(output_model.contact.contact_id)
