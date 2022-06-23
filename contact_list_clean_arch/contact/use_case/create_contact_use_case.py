import logging

from fastapi import Depends

from contact_list_clean_arch.config.bean import get_contact_command_gateway
from contact_list_clean_arch.contact.gateway.contact_command_gateway import ContactCommandGateway
from contact_list_clean_arch.contact.model.contact import Contact

logger = logging.getLogger(__name__)


class InputModel:
    def __init__(self, contact: Contact):
        self.contact = contact


class OutputModel:
    def __init__(self, contact: Contact):
        self.contact = contact


class CreateContactUseCase:
    def __init__(self, contact_command_gateway: ContactCommandGateway = Depends(get_contact_command_gateway)):
        self.__contact_command_gateway = contact_command_gateway

    def execute(self, input_model: InputModel) -> OutputModel:
        logger.info("M=execute")

        contact = self.__contact_command_gateway.save(input_model.contact)
        logger.info(f"M=execute, contact_id={contact.contact_id}")

        return OutputModel(contact)
