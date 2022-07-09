import logging

from fastapi import APIRouter, Depends

from contact_list_clean_arch.app.config.bean import get_get_user_by_id_use_case
from contact_list_clean_arch.app.user.model.user import User
from contact_list_clean_arch.app.user.use_case.get_user_by_id_use_case import InputModel

router = APIRouter()
logger = logging.getLogger(__name__)


class Response:
    user: User

    def __init__(self, user: User):
        self.user = user


@router.get("/users/{user_id}")
def get_user_by_id(user_id: str, use_case=Depends(get_get_user_by_id_use_case)) -> Response:

    input_model = InputModel(user_id=user_id)

    output = use_case.execute(input_model)

    return Response(user=output.user)
