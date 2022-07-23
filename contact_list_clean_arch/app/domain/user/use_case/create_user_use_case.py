from fastapi import Depends

from contact_list_clean_arch.app.domain.auth.gateway.cryptography_gateway import CryptographyGateway
from contact_list_clean_arch.app.domain.auth.gateway.lib.cryptography_passlib_gateway import CryptographyPasslibGateway
from contact_list_clean_arch.app.domain.email.gateway.email_gateway import EmailGateway
from contact_list_clean_arch.app.domain.email.gateway.http.email_http_gateway import EmailHttpGateway
from contact_list_clean_arch.app.domain.user.gateway.db.user_in_memory_gateway import UserInMemoryGateway
from contact_list_clean_arch.app.domain.user.gateway.user_command_gateway import UserCommandGateway
from contact_list_clean_arch.app.domain.user.model.user import User


class InputModel:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password


class OutputModel:
    def __init__(self, user_id: str):
        self.user_id = user_id


class CreateUserUseCase:
    def __init__(self,
                 user_command_gateway: UserCommandGateway = Depends(UserInMemoryGateway),
                 cryptography_gateway: CryptographyGateway = Depends(CryptographyPasslibGateway),
                 email_gateway: EmailGateway = Depends(EmailHttpGateway)):
        self.__cryptography_gateway = cryptography_gateway
        self.__user_command_gateway = user_command_gateway
        self.__email_gateway = email_gateway

    def execute(self, input_model: InputModel) -> OutputModel:

        hashed_password = self.__cryptography_gateway.hash_password(plain_password=input_model.password)

        user = User(name=input_model.name, email=input_model.email, password=hashed_password)

        user = self.__user_command_gateway.create(user=user)

        self.__email_gateway.send_wellcome_email(user=user)

        return OutputModel(user_id=user.user_id)

