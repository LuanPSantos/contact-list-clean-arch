import abc

from contact_list_clean_arch.contact.model.contact import Contact


class ContactQueryGateway(abc.ABC):
    @abc.abstractmethod
    def get_by_id(self, contact_id: int) -> Contact | None:
        pass
