import abc


class AuthorizationTokenGateway:
    @abc.abstractmethod
    def create_token(self, user_id) -> str:
        pass

    @abc.abstractmethod
    def extract_user_id(self, token) -> str:
        pass
