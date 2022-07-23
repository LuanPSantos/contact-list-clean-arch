import logging

from fastapi import APIRouter, Depends

from contact_list_clean_arch.app.domain.auth.middleware.authorization_meddleware import JWTBearerMiddleware
from contact_list_clean_arch.app.domain.user.model.user import User
from contact_list_clean_arch.app.domain.user.use_case.get_user_by_id_use_case import InputModel, GetUserByIdUseCase

router = APIRouter()
logger = logging.getLogger(__name__)


class Response:
    user: User

    def __init__(self, user: User):
        self.user = user


@router.get("/users/{user_id}",
            dependencies=[Depends(JWTBearerMiddleware())])
def get_user_by_id(user_id: str, use_case: GetUserByIdUseCase = Depends(GetUserByIdUseCase)) -> Response:

    input_model = InputModel(user_id=user_id)

    output = use_case.execute(input_model)

    return Response(user=output.user)
