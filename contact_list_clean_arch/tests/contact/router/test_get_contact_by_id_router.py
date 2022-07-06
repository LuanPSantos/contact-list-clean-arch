import uuid
from contact_list_clean_arch.app.config.db.contact_schema import ContactSchema
from contact_list_clean_arch.tests.config.integration_test_case import IntegrationTestCase


class TestGetContactByIdRouter(IntegrationTestCase):

    def test_get_contact_by_id_successfully(self):
        contact_id = str(uuid.uuid4())
        contact_schema = ContactSchema(contact_id=contact_id, name="Lucas", phone="88 8888 8888")

        self._local_session.begin()
        self._local_session.add(contact_schema)
        self._local_session.commit()

        response = self._httpClient.get(f"/contacts/{contact_id}")

        json = response.json()
        self.assertEqual(200, response.status_code)
        self.assertEqual("Lucas", json["contact"]["name"])
        self.assertEqual("88 8888 8888", json["contact"]["phone"])

    def test_get_contact_by_id_not_found(self):
        contact_id = str(uuid.uuid4())

        response = self._httpClient.get(f"/contacts/{contact_id}")

        json = response.json()

        self.assertEqual(404, response.status_code)
        self.assertEqual("Contact not found", json["message"])
