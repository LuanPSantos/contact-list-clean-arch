import abc


class AuthorizationTokenGateway:
    @abc.abstractmethod
    def create_token(self, user_id) -> str:
        pass
