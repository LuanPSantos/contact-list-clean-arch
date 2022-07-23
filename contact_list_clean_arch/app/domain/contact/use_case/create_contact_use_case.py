import logging

from fastapi import Depends

from contact_list_clean_arch.app.domain.contact.gateway.contact_command_gateway import ContactCommandGateway
from contact_list_clean_arch.app.domain.contact.gateway.db.contact_in_memory_gateway import ContactInMemoryGateway
from contact_list_clean_arch.app.domain.contact.model.contact import Contact
from contact_list_clean_arch.app.domain.user.exception.user_not_fount_exception import UserNotFoundException
from contact_list_clean_arch.app.domain.user.gateway.db.user_in_memory_gateway import UserInMemoryGateway
from contact_list_clean_arch.app.domain.user.gateway.user_query_gateway import UserQueryGateway

logger = logging.getLogger(__name__)


class InputModel:
    def __init__(self, contact: Contact):
        self.contact = contact


class OutputModel:
    def __init__(self, contact: Contact):
        self.contact = contact


class CreateContactUseCase:
    def __init__(self,
                 contact_command_gateway: ContactCommandGateway = Depends(ContactInMemoryGateway),
                 user_query_gateway: UserQueryGateway = Depends(UserInMemoryGateway)):
        self.__contact_command_gateway = contact_command_gateway
        self.__user_query_gateway = user_query_gateway

    def execute(self, input_model: InputModel) -> OutputModel:
        logger.info("M=execute")

        user = self.__user_query_gateway.get_by_id(user_id=input_model.contact.user_id)

        if user is None:
            raise UserNotFoundException()

        contact = self.__contact_command_gateway.save(input_model.contact)
        logger.info(f"M=execute, contact_id={contact.contact_id}")

        return OutputModel(contact)
