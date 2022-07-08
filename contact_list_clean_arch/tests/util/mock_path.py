from contact_list_clean_arch.app.contact.gateway.contact_command_gateway import ContactCommandGateway
from contact_list_clean_arch.app.contact.gateway.contact_query_gateway import ContactQueryGateway
from contact_list_clean_arch.app.user.gateway.user_command_gateway import UserCommandGateway
from contact_list_clean_arch.app.user.gateway.user_query_gateway import UserQueryGateway


def __path_of(clazz) -> str:
    return clazz.__module__ + '.' + clazz.__qualname__


contact_query_gateway_path = __path_of(ContactQueryGateway)
contact_command_gateway_path = __path_of(ContactCommandGateway)
user_command_gateway_path = __path_of(UserCommandGateway)
user_query_gateway_path = __path_of(UserQueryGateway)
