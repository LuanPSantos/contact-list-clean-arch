import uuid
from unittest import TestCase

from fastapi.testclient import TestClient

from contact_list_clean_arch.config.db.contact_schema import ContactSchema
from contact_list_clean_arch.main import application
from tests import start_test_session


class TestGetContactByIdRouter(TestCase):
    __httpClient = TestClient(application)

    def test_get_contact_by_id_successfully(self):
        with start_test_session() as session:
            contact_id = str(uuid.uuid4())
            contact_schema = ContactSchema(contact_id=contact_id, name="Lucas", phone="88 8888 8888")

            session.begin()

            session.add(contact_schema)

            session.commit()

        response = self.__httpClient.get(f"/contacts/{contact_id}")

        json = response.json()

        self.assertEqual(200, response.status_code)
        self.assertEqual("Lucas", json["contact"]["name"])
        self.assertEqual("88 8888 8888", json["contact"]["phone"])

