import abc

from contact_list_clean_arch.app.entity.user.model.user import User


class EmailGateway(abc.ABC):
    @abc.abstractmethod
    def send_wellcome_email(self, user: User) -> None:
        pass
