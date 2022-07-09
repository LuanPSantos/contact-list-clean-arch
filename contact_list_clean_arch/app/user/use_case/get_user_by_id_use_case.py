from contact_list_clean_arch.app.user.exception.user_not_fount_exception import UserNotFoundException
from contact_list_clean_arch.app.user.gateway.user_query_gateway import UserQueryGateway
from contact_list_clean_arch.app.user.model.user import User


class InputModel:
    user_id: str

    def __init__(self, user_id: str):
        self.user_id = user_id


class OutputModel:
    user: User

    def __init__(self, user: User):
        self.user = user


class GetUserByIdUseCase:
    def __init__(self, user_query_gateway: UserQueryGateway):
        self.user_query_gateway = user_query_gateway

    def execute(self, input_model: InputModel) -> OutputModel:

        user = self.user_query_gateway.get_by_id(input_model.user_id)

        if user is None:
            raise UserNotFoundException()

        return OutputModel(user=user)
