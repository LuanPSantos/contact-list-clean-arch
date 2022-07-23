import json

import requests_mock
from requests_mock import Mocker
from sqlalchemy import select

from contact_list_clean_arch.app.config.db.user_schema import UserSchema
from contact_list_clean_arch.app.config.security.security_config import get_crypt_context
from contact_list_clean_arch.app.domain.email.gateway.http.email_http_gateway import EMAIL_SERVICE_URL
from contact_list_clean_arch.tests.config.integration_test_case import IntegrationTestCase
from contact_list_clean_arch.tests.util.teste_factory import create_test_user


class TestCreateUserRouter(IntegrationTestCase):

    @requests_mock.Mocker(real_http=True)
    def test_create_user_successfully(self, email_server_mock: Mocker):

        email_server_mock.post(url=f"{EMAIL_SERVICE_URL}/emails/wellcome", status_code=200)

        user = create_test_user()

        response = self._http_client.post("/users", json={"name": user.name, "email": user.email, "password": user.password})

        response_body = response.json()
        self.assertIsNotNone(response_body["user_id"])
        self.assertEqual(201, response.status_code)

        user_schema = self._local_session.get(UserSchema, response_body["user_id"])

        self.assertEqual(user.name, user_schema.name)
        self.assertEqual(user.email, user_schema.email)
        self.assertTrue(self._text_crypt_context.verify(user.password, user_schema.password))

        wellcome_email_request = json.loads(email_server_mock.last_request.text)
        self.assertEqual(user.name, wellcome_email_request["user_name"])
        self.assertEqual(user.email, wellcome_email_request["user_email"])

    @requests_mock.Mocker(real_http=True)
    def test_create_user_failed_by_email_service_communication_failed(self, email_server_mock: Mocker):
        email_server_mock.post(url=f"{EMAIL_SERVICE_URL}/emails/wellcome", status_code=500)
        user = create_test_user()
        response = self._http_client.post("/users", json={"name": user.name, "email": user.email, "password": user.password})

        response_body = response.json()
        self.assertIsNotNone(response_body["message"])
        self.assertEqual(500, response.status_code)

        user_schema = self._local_session.execute(
            select(UserSchema).where(UserSchema.email == user.email)).fetchone()

        self.assertIsNone(user_schema)

