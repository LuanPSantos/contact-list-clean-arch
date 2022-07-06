from fastapi import APIRouter, Depends
import logging

from contact_list_clean_arch.app.config.bean import get_get_contact_by_id_use_case
from contact_list_clean_arch.app.contact.model.contact import Contact
from contact_list_clean_arch.app.contact.use_case.get_contact_by_id_use_case import InputModel

router = APIRouter()
logger = logging.getLogger(__name__)


class Response:
    contact: Contact

    def __init__(self, contact: Contact):
        self.contact = contact


@router.get("/contacts/{contact_id}")
def get_contact_by_id(contact_id: str, use_case=Depends(get_get_contact_by_id_use_case)) -> Response:
    logger.info(f"M=get_contact_by_id, contact_id={contact_id}")

    input_model = InputModel(contact_id)

    output_model = use_case.execute(input_model)

    return Response(output_model.contact)
