import abc


class CryptographyGateway:
    @abc.abstractmethod
    def match_password(self, plain_password, hashed_password) -> bool:
        pass

    @abc.abstractmethod
    def hash_password(self, plain_password: str) -> str:
        pass
