import uuid

import pytest

from contact_list_clean_arch.app.config.security.security_config import get_crypt_context
from contact_list_clean_arch.app.domain.auth.gateway.lib.authorization_jwt_token import AuthorizationJwtTokenGateway
from contact_list_clean_arch.app.config.db.contact_schema import ContactSchema
from contact_list_clean_arch.app.config.db.user_schema import UserSchema
from contact_list_clean_arch.app.main import application
from contact_list_clean_arch.tests.config.db import start_local_test_session
from unittest import TestCase
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from contact_list_clean_arch.tests.util.teste_factory import create_test_user, create_test_contact


class AuthInfo:
    def __init__(self, user_schema: UserSchema, token: str):
        self.user_schema = user_schema
        self.token = token


class IntegrationTestCase(TestCase):
    _http_client = TestClient(application)
    _text_crypt_context = get_crypt_context()
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

        user_schema = self._generate_user_schema()

        local_session.add(user_schema)

        local_session.commit()

        token = self.__authorization_token_gateway.create_token(user_schema.user_id)

        return AuthInfo(user_schema=user_schema, token=token)

    def _generate_user_schema(self) -> UserSchema:
        user = create_test_user()

        return UserSchema(
            user_id=user.user_id,
            name=user.name,
            email=user.email,
            password=self._text_crypt_context.hash(user.password)
        )

    def create_contact_in_db(self, user_id: str) -> ContactSchema:
        contact = create_test_contact(user_id)

        self._local_session.begin()

        contact_id = str(uuid.uuid4())
        contact_schema = ContactSchema(
            contact_id=contact_id,
            name=contact.name,
            phone=contact.phone,
            user_id=contact.user_id
        )

        self._local_session.add(contact_schema)
        self._local_session.commit()

        return contact_schema
