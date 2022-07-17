from contact_list_clean_arch.tests.config.integration_test_case import IntegrationTestCase
from contact_list_clean_arch.tests.util.constants import PLAIN_PASSWORD


class TestUserAuthenticationRouter(IntegrationTestCase):

    def test_authenticate_user(self):

        auth_info = self.create_and_authenticate_user()

        response = self._httpClient.post(f"login",
                                         json={"email": auth_info.user_schema.email, "password": PLAIN_PASSWORD})

        self.assertEqual(200, response.status_code)

        json = response.json()
        self.assertIsNotNone(json["authorization_token"])

    def test_not_authenticate_user(self):

        auth_info = self.create_and_authenticate_user()

        response = self._httpClient.post(f"login",
                                         json={"email": auth_info.user_schema.email, "password": "XX"})

        self.assertEqual(403, response.status_code)

        json = response.json()
        self.assertEqual("Invalid email or password", json["message"])
