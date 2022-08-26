import logging

from fastapi import Depends

from contact_list_clean_arch.app.entity.contact.gateway.contact_command_gateway import ContactCommandGateway
from contact_list_clean_arch.app.entity.contact.gateway.db.contact_db_gateway import ContactDBGateway
from contact_list_clean_arch.app.entity.contact.model.contact import Contact
from contact_list_clean_arch.app.entity.user.exception.user_not_fount_exception import UserNotFoundException
from contact_list_clean_arch.app.entity.user.gateway.db.user_db_gateway import UserDBGateway
from contact_list_clean_arch.app.entity.user.gateway.user_query_gateway import UserQueryGateway

logger = logging.getLogger(__name__)


class InputModel:
    def __init__(self, contact: Contact):
        self.contact = contact


class OutputModel:
    def __init__(self, contact: Contact):
        self.contact = contact


class CreateContactUseCase:
    def __init__(self,
                 contact_command_gateway: ContactCommandGateway = Depends(ContactDBGateway),
                 user_query_gateway: UserQueryGateway = Depends(UserDBGateway)):
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
