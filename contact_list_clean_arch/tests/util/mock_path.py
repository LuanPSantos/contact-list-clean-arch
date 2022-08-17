from contact_list_clean_arch.app.entity.auth.gateway.authorization_token_gateway import AuthorizationTokenGateway
from contact_list_clean_arch.app.entity.auth.gateway.cryptography_gateway import CryptographyGateway
from contact_list_clean_arch.app.entity.contact.gateway.contact_command_gateway import ContactCommandGateway
from contact_list_clean_arch.app.entity.contact.gateway.contact_query_gateway import ContactQueryGateway
from contact_list_clean_arch.app.entity.email.gateway.email_gateway import EmailGateway
from contact_list_clean_arch.app.entity.user.gateway.user_command_gateway import UserCommandGateway
from contact_list_clean_arch.app.entity.user.gateway.user_query_gateway import UserQueryGateway


def __path_of(clazz) -> str:
    return clazz.__module__ + '.' + clazz.__qualname__


contact_query_gateway_path = __path_of(ContactQueryGateway)
contact_command_gateway_path = __path_of(ContactCommandGateway)
user_command_gateway_path = __path_of(UserCommandGateway)
user_query_gateway_path = __path_of(UserQueryGateway)
cryptography_gateway_path = __path_of(CryptographyGateway)
authorization_token_gateway_path = __path_of(AuthorizationTokenGateway)
email_gateway_path = __path_of(EmailGateway)
