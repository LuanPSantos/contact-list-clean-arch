import abc

from contact_list_clean_arch.app.user.model.user import User


class UserQueryGateway(abc.ABC):
    @abc.abstractmethod
    def get_by_id(self, user_id: str) -> User | None:
        pass
