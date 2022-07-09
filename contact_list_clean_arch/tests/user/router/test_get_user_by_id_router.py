import uuid

from contact_list_clean_arch.app.config.db.user_schema import UserSchema
from contact_list_clean_arch.tests.config.integration_test_case import IntegrationTestCase


class TestGetUserByIdRouter(IntegrationTestCase):

    def test_get_user_by_id_successfully(self):
        self._local_session.begin()

        user_id = str(uuid.uuid4())
        user_schema = UserSchema(user_id=user_id, name="Vau", email="vau@email.com", password="123")

        self._local_session.add(user_schema)
        self._local_session.commit()

        response = self._httpClient.get(f"users/{user_id}")

        json = response.json()
        self.assertEqual(200, response.status_code)
        self.assertEqual("Vau", json["user"]["name"])
        self.assertEqual("vau@email.com", json["user"]["email"])
        self.assertEqual("123", json["user"]["password"])

    def test_get_user_by_id_not_found(self):

        response = self._httpClient.get(f"users/1")

        json = response.json()

        self.assertEqual(404, response.status_code)
        self.assertEqual("User not found", json["message"])
