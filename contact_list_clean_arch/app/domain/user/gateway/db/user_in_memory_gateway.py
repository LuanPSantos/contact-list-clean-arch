import uuid

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from contact_list_clean_arch.app.config.db import start_session
from contact_list_clean_arch.app.config.db.user_schema import UserSchema
from contact_list_clean_arch.app.domain.user.gateway.user_command_gateway import UserCommandGateway
from contact_list_clean_arch.app.domain.user.gateway.user_query_gateway import UserQueryGateway
from contact_list_clean_arch.app.domain.user.model.user import User


class UserInMemoryGateway(UserCommandGateway, UserQueryGateway):

    def __init__(self, session: Session = Depends(start_session)):
        super().__init__()
        self.__session = session

    def create(self, user: User) -> User:

        user_schema = UserSchema(user_id=str(uuid.uuid4()), name=user.name, email=user.email, password=user.password)

        self.__session.add(user_schema)

        return User(
            user_id=user_schema.user_id,
            name=user_schema.name,
            email=user_schema.email,
            password=user_schema.password
        )

    def get_by_id(self, user_id: str) -> User | None:

        user_schema = self.__session.get(UserSchema, user_id)

        if user_schema is None:
            return None

        return User(
            user_id=user_schema.user_id,
            name=user_schema.name,
            email=user_schema.email,
            password=user_schema.password
        )

    def get_by_email(self, email: str) -> User | None:

        user_schema = self.__session.execute(select(UserSchema).where(UserSchema.email == email)).fetchone()[0]

        if user_schema is None:
            return None

        return User(
            user_id=user_schema.user_id,
            name=user_schema.name,
            email=user_schema.email,
            password=user_schema.password
        )
