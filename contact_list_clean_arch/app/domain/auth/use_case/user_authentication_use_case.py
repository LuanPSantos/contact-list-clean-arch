from contact_list_clean_arch.app.domain.auth.exception.UnauthenticatedException import UnauthenticatedException
from contact_list_clean_arch.app.domain.auth.gateway.authorization_token_gateway import AuthorizationTokenGateway
from contact_list_clean_arch.app.domain.auth.gateway.cryptography_gateway import CryptographyGateway
from contact_list_clean_arch.app.domain.user.gateway.user_query_gateway import UserQueryGateway


class InputModel:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password


class OutputModel:
    def __init__(self, authorization_token: str):
        self.authorization_token = authorization_token


class UserAuthenticationUseCase:
    def __init__(self,
                 user_query_gateway: UserQueryGateway,
                 crytography_gateway: CryptographyGateway,
                 authorization_token_gateway: AuthorizationTokenGateway):

        self.user_query_gateway = user_query_gateway
        self.crytography_gateway = crytography_gateway
        self.authorization_token_gateway = authorization_token_gateway

    def execute(self, input_model: InputModel) -> OutputModel:

        user = self.user_query_gateway.get_by_email(input_model.email)

        if user is None:
            raise UnauthenticatedException()

        password_matched = self.crytography_gateway.match_password(input_model.password, user.password)

        if not password_matched:
            raise UnauthenticatedException()

        authorization_token = self.authorization_token_gateway.create_token(user_id=user.user_id)

        return OutputModel(authorization_token=authorization_token)
