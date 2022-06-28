from contact_list_clean_arch.app.contact.gateway.contact_command_gateway import ContactCommandGateway
from contact_list_clean_arch.app.contact.gateway.contact_query_gateway import ContactQueryGateway

contact_query_gateway_path = ContactQueryGateway.__module__ + '.' + ContactQueryGateway.__qualname__
contact_command_gateway_path = ContactCommandGateway.__module__ + '.' + ContactCommandGateway.__qualname__
