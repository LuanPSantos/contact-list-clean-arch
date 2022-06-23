from fastapi import APIRouter
import logging

from sqlalchemy.orm import Session

from contact_list_clean_arch.config.db.db_config import start_session, engine
from contact_list_clean_arch.config.exception_handler import with_exception_handler
from contact_list_clean_arch.contact.gateway.db.contact_command_my_sql_gateway import ContactInMemoryGateway
from contact_list_clean_arch.contact.model.contact import Contact
from contact_list_clean_arch.contact.use_case.get_contact_by_id_use_case import GetContactByIdUseCase, InputModel

router = APIRouter()
logger = logging.getLogger(__name__)


class Response:
    contact: Contact

    def __init__(self, contact: Contact):
        self.contact = contact


@router.get("/contacts/{contact_id}")
def get_contact_by_id(contact_id: str) -> Response:
    logger.info(f"M=get_contact_by_id, contact_id={contact_id}")

    with Session(engine) as session:
        use_case = GetContactByIdUseCase(ContactInMemoryGateway(session))

        input_model = InputModel(contact_id)

        output_model = with_exception_handler(lambda: use_case.execute(input_model))

    return Response(output_model.contact)
