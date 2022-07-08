import abc

from contact_list_clean_arch.app.user.model.user import User


class UserCommandGateway(abc.ABC):
    @abc.abstractmethod
    def create(self, user: User) -> User:
        pass
