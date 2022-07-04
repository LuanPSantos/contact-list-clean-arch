
from contact_list_clean_arch.app.config.db.contact_schema import ContactSchema
from contact_list_clean_arch.tests.config.integration_test_case import IntegrationTestCase


class TestCreateContactRouter(IntegrationTestCase):

    def test_create_contact_successfully(self):
        response = self._httpClient.post("/contacts", json={"name": "Luan", "phone": "99 9999 9999"})

        json = response.json()
        self.assertIsNotNone(json["contact_id"])
        self.assertEqual(201, response.status_code)

        contact_schema = self._local_session.get(ContactSchema, json["contact_id"])

        self.assertEqual("Luan", contact_schema.name)
        self.assertEqual("99 9999 9999", contact_schema.phone)
