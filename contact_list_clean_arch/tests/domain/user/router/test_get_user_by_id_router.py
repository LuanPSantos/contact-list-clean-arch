
from contact_list_clean_arch.tests.config.integration_test_case import IntegrationTestCase


class TestGetUserByIdRouter(IntegrationTestCase):

    def test_get_user_by_id_successfully(self):
        auth_info = self.create_and_authenticate_user()

        response = self._httpClient.get(f"users/{auth_info.user_schema.user_id}",
                                        headers={"Authorization": auth_info.token})

        json = response.json()
        self.assertEqual(200, response.status_code)
        self.assertEqual(auth_info.user_schema.name, json["user"]["name"])
        self.assertEqual(auth_info.user_schema.email, json["user"]["email"])
        self.assertEqual(auth_info.user_schema.password, json["user"]["password"])

    def test_get_user_by_id_not_found(self):

        auth_info = self.create_and_authenticate_user()

        response = self._httpClient.get(f"users/1", headers={"Authorization": auth_info.token})

        json = response.json()

        self.assertEqual(404, response.status_code)
        self.assertEqual("User not found", json["message"])

    def test_not_get_user_by_id_due_unauthenticated(self):
        auth_info = self.create_and_authenticate_user()

        response = self._httpClient.get(f"users/{auth_info.user_schema.user_id}")

        self.assertEqual(403, response.status_code)
