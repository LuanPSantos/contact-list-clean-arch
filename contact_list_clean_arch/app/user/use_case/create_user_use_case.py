from contact_list_clean_arch.app.user.gateway.user_command_gateway import UserCommandGateway
from contact_list_clean_arch.app.user.model.user import User


class InputModel:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password


class OutputModel:
    def __init__(self, user_id: str):
        self.user_id = user_id


class CreateUserUseCase:
    def __init__(self, user_command_gateway: UserCommandGateway):
        self.__user_command_gateway = user_command_gateway

    def execute(self, input_model: InputModel) -> OutputModel:

        user = User(name=input_model.name, email=input_model.email, password=input_model.password)

        user = self.__user_command_gateway.create(user)

        return OutputModel(user_id=user.user_id)

