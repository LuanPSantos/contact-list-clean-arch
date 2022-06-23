from fastapi import Depends

from contact_list_clean_arch.config.db import start_session
from contact_list_clean_arch.contact.gateway.contact_command_gateway import ContactCommandGateway
from contact_list_clean_arch.contact.gateway.contact_query_gateway import ContactQueryGateway
from contact_list_clean_arch.contact.gateway.db.contact_command_my_sql_gateway import ContactInMemoryGateway


def get_contact_command_gateway(session=Depends(start_session)) -> ContactCommandGateway:
    return ContactInMemoryGateway(session)


def get_contact_query_gateway(session=Depends(start_session)) -> ContactQueryGateway:
    return ContactInMemoryGateway(session)
