import uuid

from fastapi import Depends

from contact_list_clean_arch.config.db import start_session
from contact_list_clean_arch.config.db.contact_schema import ContactSchema
from contact_list_clean_arch.contact.gateway.contact_command_gateway import ContactCommandGateway
from contact_list_clean_arch.contact.gateway.contact_query_gateway import ContactQueryGateway
from contact_list_clean_arch.contact.model.contact import Contact


class ContactInMemoryGateway(ContactCommandGateway, ContactQueryGateway):
    def __init__(self, session=Depends(start_session)):
        super().__init__()
        self.__session = session

    def get_by_id(self, contact_id: str) -> Contact | None:

        contact_schema = self.__session.get(ContactSchema, contact_id)

        if contact_schema is None:
            return None

        return Contact(
            contact_id=contact_schema.contact_id,
            name=contact_schema.name,
            phone=contact_schema.phone
        )

    def save(self, contact: Contact) -> Contact:

        contact_schema = ContactSchema(contact_id=str(uuid.uuid4()), name=contact.name, phone=contact.phone)

        self.__session.begin()

        self.__session.add(contact_schema)

        self.__session.commit()

        return Contact(
            contact_id=contact_schema.contact_id,
            name=contact_schema.name,
            phone=contact_schema.phone
        )
