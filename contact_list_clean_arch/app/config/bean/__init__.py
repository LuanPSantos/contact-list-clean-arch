from fastapi import Depends

from contact_list_clean_arch.app.config.db import start_session
from contact_list_clean_arch.app.contact.gateway.contact_command_gateway import ContactCommandGateway
from contact_list_clean_arch.app.contact.gateway.contact_query_gateway import ContactQueryGateway
from contact_list_clean_arch.app.contact.gateway.db.contact_command_my_sql_gateway import ContactInMemoryGateway
from contact_list_clean_arch.app.contact.use_case.create_contact_use_case import CreateContactUseCase
from contact_list_clean_arch.app.contact.use_case.get_contact_by_id_use_case import GetContactByIdUseCase


def get_contact_command_gateway(session=Depends(start_session)) -> ContactCommandGateway:
    return ContactInMemoryGateway(session)


def get_contact_query_gateway(session=Depends(start_session)) -> ContactQueryGateway:
    return ContactInMemoryGateway(session)


def get_create_contact_use_case(contact_command_gateway=Depends(get_contact_command_gateway)) -> CreateContactUseCase:
    return CreateContactUseCase(contact_command_gateway)


def get_get_contact_by_id_use_case(contact_query_gateway=Depends(get_contact_query_gateway)) -> GetContactByIdUseCase:
    return GetContactByIdUseCase(contact_query_gateway)
