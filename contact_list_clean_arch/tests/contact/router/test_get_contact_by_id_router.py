import uuid
from contact_list_clean_arch.tests.config.integration_test_case import IntegrationTestCase


class TestGetContactByIdRouter(IntegrationTestCase):

    def test_get_contact_by_id_successfully(self):
        auth_info = self.create_and_authenticate_user()
        contact_schema = self.create_contact_in_db(auth_info.user_schema.user_id)

        response = self._httpClient.get(f"users/{auth_info.user_schema.user_id}/contacts/{contact_schema.contact_id}",
                                        headers={"Authorization": auth_info.token})

        json = response.json()
        self.assertEqual(200, response.status_code)
        self.assertEqual(contact_schema.name, json["contact"]["name"])
        self.assertEqual(contact_schema.phone, json["contact"]["phone"])

    def test_get_contact_by_id_not_found(self):
        auth_info = self.create_and_authenticate_user()

        contact_id = str(uuid.uuid4())

        response = self._httpClient.get(f"users/{auth_info.user_schema.user_id}/contacts/{contact_id}",
                                        headers={"Authorization": auth_info.token})

        json = response.json()

        self.assertEqual(404, response.status_code)
        self.assertEqual("Contact not found", json["message"])
