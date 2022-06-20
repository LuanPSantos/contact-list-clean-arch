import uuid

from contact_list_clean_arch.config.db.db_config import ContactSchema
from contact_list_clean_arch.contact.gateway.contact_command_gateway import ContactCommandGateway
from contact_list_clean_arch.contact.gateway.contact_query_gateway import ContactQueryGateway
from contact_list_clean_arch.contact.model.contact import Contact


class ContactInMemoryGateway(ContactCommandGateway, ContactQueryGateway):
    def __init__(self, get_session):
        super().__init__()
        self.__get_session = get_session

    def get_by_id(self, contact_id: int) -> Contact | None:

        if contact_id != 1:
            return None

        return Contact(
            contact_id=1,
            name="Luan",
            phone="99 99999 9999"
        )

    def save(self, contact: Contact) -> Contact:
        session = self.__get_session()

        contact_schema = ContactSchema(contact_id=str(uuid.uuid4()), name=contact.name, phone=contact.phone)

        session.add(contact_schema)
        session.flush()

        #print(contact_schema)
        return Contact(
            contact_id=None,
            name="contact_schema.name",
            phone="contact_schema.phone"
        )
