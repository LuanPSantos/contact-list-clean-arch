import uuid
from random import randint

import pytest

from contact_list_clean_arch.app.auth.gateway.lib.authorization_jwt_token import AuthorizationJwtTokenGateway
from contact_list_clean_arch.app.config.db.contact_schema import ContactSchema
from contact_list_clean_arch.app.config.db.user_schema import UserSchema
from contact_list_clean_arch.app.main import application
from contact_list_clean_arch.tests.config.db import start_local_test_session
from unittest import TestCase
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


class AuthInfo:
    def __init__(self, user_schema: UserSchema, token: str):
        self.user_schema = user_schema
        self.token = token


def _generate_user_schema() -> UserSchema:
    random = f"{uuid.uuid4()}[-12:]"
    user_id = str(uuid.uuid4())
    name = str(f"Name {random} da Silva")
    email = str(f"email.{random}@test.com")
    password = str(uuid.uuid4())

    return UserSchema(user_id=user_id, name=name, email=email, password=password)


class IntegrationTestCase(TestCase):
    _httpClient = TestClient(application)

    __local_session: Session
    __authorization_token_gateway = AuthorizationJwtTokenGateway()

    @pytest.fixture(autouse=True)
    def run_before_and_after_tests(self):

        self._local_session = start_local_test_session()
        print("---- BEFORE TEST ----")
        yield
        print("---- AFTER TEST ----")
        self._local_session.close()

    def create_and_authenticate_user(self) -> AuthInfo:
        local_session = start_local_test_session()
        local_session.begin()

        user_schema = _generate_user_schema()

        local_session.add(user_schema)

        local_session.commit()

        token = self.__authorization_token_gateway.create_token(user_schema.user_id)

        return AuthInfo(user_schema=user_schema, token=token)

    def create_contact(self, user_id: str) -> ContactSchema:
        random = f"{uuid.uuid4()}[-12:]"
        name = str(f"Name {random} da Silva")
        phone = str(f"({randint(10, 99)}) {randint(10000, 99999)}-{randint(1000, 9999)}")

        self._local_session.begin()

        contact_id = str(uuid.uuid4())
        contact_schema = ContactSchema(contact_id=contact_id, name=name, phone=phone, user_id=user_id)

        self._local_session.add(contact_schema)
        self._local_session.commit()

        return contact_schema
