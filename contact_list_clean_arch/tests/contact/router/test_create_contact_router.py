import uuid
from contact_list_clean_arch.app.config.db.contact_schema import ContactSchema
from contact_list_clean_arch.app.config.db.user_schema import UserSchema
from contact_list_clean_arch.tests.config.integration_test_case import IntegrationTestCase


class TestCreateContactRouter(IntegrationTestCase):

    def test_create_contact_successfully(self):
        self._local_session.begin()
        user_id = str(uuid.uuid4())
        user_schema = UserSchema(user_id=user_id, name="Joao", email="joao@email.com", password="123")
        self._local_session.add(user_schema)
        self._local_session.flush()

        response = self._httpClient.post(f"users/{user_id}/contacts", json={"name": "Luan", "phone": "99 9999 9999"})

        self.assertEqual(201, response.status_code)

        json = response.json()
        self.assertIsNotNone(json["contact_id"])

        contact_schema = self._local_session.get(ContactSchema, json["contact_id"])

        self.assertEqual("Luan", contact_schema.name)
        self.assertEqual("99 9999 9999", contact_schema.phone)
