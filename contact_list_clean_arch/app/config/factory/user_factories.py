from fastapi import Depends

from contact_list_clean_arch.app.config.factory.auth_factories import get_crytography_gateway
from contact_list_clean_arch.app.config.db import start_session

from contact_list_clean_arch.app.domain.user.gateway.db.user_in_memory_gateway import UserInMemoryGateway
from contact_list_clean_arch.app.domain.user.gateway.user_command_gateway import UserCommandGateway
from contact_list_clean_arch.app.domain.user.use_case.create_user_use_case import CreateUserUseCase
from contact_list_clean_arch.app.domain.user.use_case.get_user_by_id_use_case import GetUserByIdUseCase
from contact_list_clean_arch.app.domain.user.gateway.user_query_gateway import UserQueryGateway



