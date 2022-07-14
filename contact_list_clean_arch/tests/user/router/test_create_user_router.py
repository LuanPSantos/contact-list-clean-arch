from contact_list_clean_arch.app.config.db.user_schema import UserSchema
from contact_list_clean_arch.app.config.security.security_config import crypt_context
from contact_list_clean_arch.tests.config.integration_test_case import IntegrationTestCase


class TestCreateUserRouter(IntegrationTestCase):

    def test_create_user_successfully(self):
        response = self._httpClient.post("/users", json={"name": "Jose", "email": "jose@email.com", "password": "123"})

        json = response.json()
        self.assertIsNotNone(json["user_id"])
        self.assertEqual(201, response.status_code)

        user_schema = self._local_session.get(UserSchema, json["user_id"])

        self.assertEqual("Jose", user_schema.name)
        self.assertEqual("jose@email.com", user_schema.email)
        self.assertTrue(crypt_context.verify("123", user_schema.password))
