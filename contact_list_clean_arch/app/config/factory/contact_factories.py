from fastapi import Depends

from contact_list_clean_arch.app.config.factory.user_factories import get_user_query_gateway
from contact_list_clean_arch.app.config.db import start_session
from contact_list_clean_arch.app.domain.contact.gateway.contact_command_gateway import ContactCommandGateway
from contact_list_clean_arch.app.domain.contact.gateway.contact_query_gateway import ContactQueryGateway
from contact_list_clean_arch.app.domain.contact.gateway.db.contact_in_memory_gateway import ContactInMemoryGateway
from contact_list_clean_arch.app.domain.contact.use_case.create_contact_use_case import CreateContactUseCase
from contact_list_clean_arch.app.domain.contact.use_case.get_contact_by_id_use_case import GetContactByIdUseCase


