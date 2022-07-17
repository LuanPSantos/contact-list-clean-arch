from fastapi import Depends

from contact_list_clean_arch.app.domain.auth.gateway.authorization_token_gateway import AuthorizationTokenGateway
from contact_list_clean_arch.app.domain.auth.gateway.cryptography_gateway import CryptographyGateway
from contact_list_clean_arch.app.domain.auth.gateway.lib.authorization_jwt_token import AuthorizationJwtTokenGateway
from contact_list_clean_arch.app.domain.auth.gateway.lib.cryptography_passlib_gateway import CryptographyPasslibGateway
from contact_list_clean_arch.app.domain.auth.use_case.user_authentication_use_case import UserAuthenticationUseCase
from contact_list_clean_arch.app.config.db import start_session
from contact_list_clean_arch.app.config.security.security_config import crypt_context
from contact_list_clean_arch.app.domain.contact.gateway.contact_command_gateway import ContactCommandGateway
from contact_list_clean_arch.app.domain.contact.gateway.contact_query_gateway import ContactQueryGateway
from contact_list_clean_arch.app.domain.contact.gateway.db.contact_in_memory_gateway import ContactInMemoryGateway
from contact_list_clean_arch.app.domain.contact.use_case.create_contact_use_case import CreateContactUseCase
from contact_list_clean_arch.app.domain.contact.use_case.get_contact_by_id_use_case import GetContactByIdUseCase
from contact_list_clean_arch.app.domain.user.gateway.db.user_in_memory_gateway import UserInMemoryGateway
from contact_list_clean_arch.app.domain.user.gateway.user_command_gateway import UserCommandGateway

from contact_list_clean_arch.app.domain.user.gateway.user_query_gateway import UserQueryGateway
from contact_list_clean_arch.app.domain.user.use_case.create_user_use_case import CreateUserUseCase
from contact_list_clean_arch.app.domain.user.use_case.get_user_by_id_use_case import GetUserByIdUseCase


# TODO separar factories
def get_contact_command_gateway(session=Depends(start_session)) -> ContactCommandGateway:
    return ContactInMemoryGateway(session)


def get_contact_query_gateway(session=Depends(start_session)) -> ContactQueryGateway:
    return ContactInMemoryGateway(session)


def get_user_command_gateway(session=Depends(start_session)) -> UserCommandGateway:
    return UserInMemoryGateway(session)


def get_user_query_gateway(session=Depends(start_session)) -> UserQueryGateway:
    return UserInMemoryGateway(session)


def get_crytography_gateway() -> CryptographyGateway:
    return CryptographyPasslibGateway(crypt_context)


def get_authorization_token_gateway() -> AuthorizationTokenGateway:
    return AuthorizationJwtTokenGateway()


def get_create_contact_use_case(contact_command_gateway=Depends(get_contact_command_gateway),
                                user_query_gateway=Depends(get_user_query_gateway)) -> CreateContactUseCase:
    return CreateContactUseCase(contact_command_gateway, user_query_gateway)


def get_get_contact_by_id_use_case(contact_query_gateway=Depends(get_contact_query_gateway)) -> GetContactByIdUseCase:
    return GetContactByIdUseCase(contact_query_gateway)


def get_create_user_use_case(user_command_gateway=Depends(get_user_command_gateway),
                             cryptography_gateway=Depends(get_crytography_gateway)) -> CreateUserUseCase:
    return CreateUserUseCase(user_command_gateway, cryptography_gateway)


def get_get_user_by_id_use_case(user_query_gateway=Depends(get_user_query_gateway)) -> GetUserByIdUseCase:
    return GetUserByIdUseCase(user_query_gateway)


def get_user_authentication_use_case(user_query_gateway=Depends(get_user_query_gateway),
                                     cryptography_gateway=Depends(get_crytography_gateway),
                                     authorization_token_gateway=Depends(get_authorization_token_gateway)):
    return UserAuthenticationUseCase(user_query_gateway, cryptography_gateway, authorization_token_gateway)
