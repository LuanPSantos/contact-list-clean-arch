import logging

from contact_list_clean_arch.app.contact.exception.contact_not_found_exception import ContactNotFoundException
from contact_list_clean_arch.app.contact.gateway.contact_query_gateway import ContactQueryGateway
from contact_list_clean_arch.app.contact.model.contact import Contact

logger = logging.getLogger(__name__)


class InputModel:
    def __init__(self, contact_id: str, user_id: str):
        self.contact_id = contact_id
        self.user_id = user_id


class OutputModel:
    def __init__(self, contact: Contact):
        self.contact = contact


class GetContactByIdUseCase:
    def __init__(self, contact_query_gateway: ContactQueryGateway):
        self.contact_query_gateway = contact_query_gateway

    def execute(self, input_model: InputModel) -> OutputModel:
        logger.info(f"M=execute, contact_id={input_model.contact_id}")

        contact = self.contact_query_gateway.get_by_id(input_model.contact_id)

        if contact is None or contact.user_id != input_model.user_id:
            logger.error(f"M=execute, exception=ContactNotFoundException")
            raise ContactNotFoundException()

        return OutputModel(contact)
