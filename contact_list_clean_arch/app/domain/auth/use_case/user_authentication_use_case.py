from fastapi import Depends

from contact_list_clean_arch.app.domain.auth.exception.unauthenticated_exception import UnauthenticatedException
from contact_list_clean_arch.app.domain.auth.gateway.authorization_token_gateway import AuthorizationTokenGateway
from contact_list_clean_arch.app.domain.auth.gateway.cryptography_gateway import CryptographyGateway
from contact_list_clean_arch.app.domain.auth.gateway.lib.authorization_jwt_token import AuthorizationJwtTokenGateway
from contact_list_clean_arch.app.domain.auth.gateway.lib.cryptography_passlib_gateway import CryptographyPasslibGateway
from contact_list_clean_arch.app.domain.user.gateway.db.user_in_memory_gateway import UserInMemoryGateway
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
                 user_query_gateway: UserQueryGateway = Depends(UserInMemoryGateway),
                 cryptography_gateway: CryptographyGateway = Depends(CryptographyPasslibGateway),
                 authorization_token_gateway: AuthorizationTokenGateway = Depends(AuthorizationJwtTokenGateway)):

        self.__user_query_gateway = user_query_gateway
        self.__cryptography_gateway = cryptography_gateway
        self.__authorization_token_gateway = authorization_token_gateway

    def execute(self, input_model: InputModel) -> OutputModel:

        user = self.__user_query_gateway.get_by_email(email=input_model.email)

        if user is None:
            raise UnauthenticatedException()

        password_matched = self.__cryptography_gateway.match_password(
            plain_password=input_model.password,
            hashed_password=user.password
        )

        if not password_matched:
            raise UnauthenticatedException()

        authorization_token = self.__authorization_token_gateway.create_token(user_id=user.user_id)

        return OutputModel(authorization_token=authorization_token)
