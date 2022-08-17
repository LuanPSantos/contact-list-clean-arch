
from contact_list_clean_arch.app.infrastructure.config.db.contact_schema import ContactSchema
from contact_list_clean_arch.tests.infrastructure.config.integration_test_case import IntegrationTestCase


class TestCreateContactRouter(IntegrationTestCase):

    def test_create_contact_successfully(self):

        auth_info = self.create_and_authenticate_user()

        response = self._http_client.post(f"users/{auth_info.user_schema.user_id}/contacts",
                                          json={"name": "Luan", "phone": "99 9999 9999"},
                                          headers={"Authorization": auth_info.token})

        self.assertEqual(201, response.status_code)

        json = response.json()
        self.assertIsNotNone(json["contact_id"])

        contact_schema = self._local_session.get(ContactSchema, json["contact_id"])

        self.assertEqual("Luan", contact_schema.name)
        self.assertEqual("99 9999 9999", contact_schema.phone)

    def test_not_create_contact_due_unauthenticated(self):
        auth_info = self.create_and_authenticate_user()

        response = self._http_client.post(f"users/{auth_info.user_schema.user_id}/contacts",
                                          json={"name": "Luan", "phone": "99 9999 9999"})

        self.assertEqual(403, response.status_code)
