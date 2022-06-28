from unittest import TestCase
from fastapi.testclient import TestClient

from contact_list_clean_arch.app.config.db.contact_schema import ContactSchema
from contact_list_clean_arch.app.main import application
from contact_list_clean_arch.tests import start_test_session


class TestGetContactByIdRouter(TestCase):
    __httpClient = TestClient(application)

    def test_create_contact_successfully(self):
        response = self.__httpClient.post("/contacts", json={"name": "Luan", "phone": "99 9999 9999"})

        json = response.json()
        self.assertIsNotNone(json["contact_id"])
        self.assertEqual(201, response.status_code)

        with start_test_session() as session:
            contact_schema = session.get(ContactSchema, json["contact_id"])

            self.assertEqual("Luan", contact_schema.name)
            self.assertEqual("99 9999 9999", contact_schema.phone)
