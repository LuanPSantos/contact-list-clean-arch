from fastapi import APIRouter, Depends
import logging

from contact_list_clean_arch.app.domain.auth.middleware.authorization_meddleware import JWTBearerMiddleware
from contact_list_clean_arch.app.domain.contact.model.contact import Contact
from contact_list_clean_arch.app.domain.contact.use_case.get_contact_by_id_use_case import InputModel, \
    GetContactByIdUseCase

router = APIRouter()
logger = logging.getLogger(__name__)


class Response:
    contact: Contact

    def __init__(self, contact: Contact):
        self.contact = contact


@router.get("/users/{user_id}/contacts/{contact_id}",
            dependencies=[Depends(JWTBearerMiddleware())])
def get_contact_by_id(user_id: str, contact_id: str,
                      use_case: GetContactByIdUseCase = Depends(GetContactByIdUseCase)) -> Response:
    logger.info(f"M=get_contact_by_id, contact_id={contact_id}, user_id={user_id}")

    input_model = InputModel(contact_id, user_id)

    output_model = use_case.execute(input_model)

    return Response(output_model.contact)
