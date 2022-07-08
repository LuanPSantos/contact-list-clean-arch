from fastapi import Depends

from contact_list_clean_arch.app.config.db import start_session
from contact_list_clean_arch.app.contact.gateway.contact_command_gateway import ContactCommandGateway
from contact_list_clean_arch.app.contact.gateway.contact_query_gateway import ContactQueryGateway
from contact_list_clean_arch.app.contact.gateway.db.contact_in_memory_gateway import ContactInMemoryGateway
from contact_list_clean_arch.app.contact.use_case.create_contact_use_case import CreateContactUseCase
from contact_list_clean_arch.app.contact.use_case.get_contact_by_id_use_case import GetContactByIdUseCase
from contact_list_clean_arch.app.user.gateway.db.user_in_memory_gateway import UserInMemoryGateway
from contact_list_clean_arch.app.user.gateway.user_command_gateway import UserCommandGateway
from contact_list_clean_arch.app.user.gateway.user_query_gateway import UserQueryGateway
from contact_list_clean_arch.app.user.use_case.create_user_use_case import CreateUserUseCase


def get_contact_command_gateway(session=Depends(start_session)) -> ContactCommandGateway:
    return ContactInMemoryGateway(session)


def get_contact_query_gateway(session=Depends(start_session)) -> ContactQueryGateway:
    return ContactInMemoryGateway(session)


def get_user_command_gateway(session=Depends(start_session)) -> UserCommandGateway:
    return UserInMemoryGateway(session)


def get_user_query_gateway(session=Depends(start_session)) -> UserQueryGateway:
    return UserInMemoryGateway(session)


def get_create_contact_use_case(contact_command_gateway=Depends(get_contact_command_gateway),
                                user_query_gateway=Depends(get_user_query_gateway)) -> CreateContactUseCase:
    return CreateContactUseCase(contact_command_gateway, user_query_gateway)


def get_get_contact_by_id_use_case(contact_query_gateway=Depends(get_contact_query_gateway)) -> GetContactByIdUseCase:
    return GetContactByIdUseCase(contact_query_gateway)


def get_create_user_use_case(user_command_gateway=Depends(get_user_command_gateway)) -> CreateUserUseCase:
    return CreateUserUseCase(user_command_gateway)
