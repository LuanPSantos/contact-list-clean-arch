import uuid
from contact_list_clean_arch.app.config.db.contact_schema import ContactSchema
from contact_list_clean_arch.app.config.db.user_schema import UserSchema
from contact_list_clean_arch.tests.config.integration_test_case import IntegrationTestCase


class TestGetContactByIdRouter(IntegrationTestCase):

    def test_get_contact_by_id_successfully(self):
        self._local_session.begin()

        user_id = str(uuid.uuid4())
        user_schema = UserSchema(user_id=user_id, name="Kato", email="kato@email.com", password="123")

        contact_id = str(uuid.uuid4())
        contact_schema = ContactSchema(contact_id=contact_id, name="Lucas", phone="88 8888 8888", user_id=user_id)

        self._local_session.add(user_schema)
        self._local_session.add(contact_schema)
        self._local_session.commit()

        response = self._httpClient.get(f"users/{user_schema.user_id}/contacts/{contact_id}")

        json = response.json()
        self.assertEqual(200, response.status_code)
        self.assertEqual("Lucas", json["contact"]["name"])
        self.assertEqual("88 8888 8888", json["contact"]["phone"])

    def test_get_contact_by_id_not_found(self):
        self._local_session.begin()
        user_id = str(uuid.uuid4())
        user_schema = UserSchema(user_id=user_id, name="Nara", email="nara@email.com", password="123")
        self._local_session.add(user_schema)
        self._local_session.commit()

        contact_id = str(uuid.uuid4())

        response = self._httpClient.get(f"users/{user_schema.user_id}/contacts/{contact_id}")

        json = response.json()

        self.assertEqual(404, response.status_code)
        self.assertEqual("Contact not found", json["message"])
