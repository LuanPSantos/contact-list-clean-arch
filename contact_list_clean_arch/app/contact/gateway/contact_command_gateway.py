import abc

from contact_list_clean_arch.app.contact.model.contact import Contact


class ContactCommandGateway(abc.ABC):
    @abc.abstractmethod
    def save(self, contact: Contact) -> Contact:
        pass
