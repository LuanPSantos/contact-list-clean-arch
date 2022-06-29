from unittest import TestCase

import pytest
from fastapi.testclient import TestClient

from contact_list_clean_arch.app.config.db.contact_schema import ContactSchema
from contact_list_clean_arch.app.main import application
from contact_list_clean_arch.tests.config.db import start_local_test_session


class TestCreateContactRouter(TestCase):
    __httpClient = TestClient(application)

    @pytest.fixture(autouse=True)
    def run_before_and_after_tests(self):
        print("===> TestCreateContactRouter")

        self.__local_session = start_local_test_session()

        yield

        self.__local_session.close()

    def test_create_contact_successfully(self):
        response = self.__httpClient.post("/contacts", json={"name": "Luan", "phone": "99 9999 9999"})

        json = response.json()
        self.assertIsNotNone(json["contact_id"])
        self.assertEqual(201, response.status_code)

        contact_schema = self.__local_session.get(ContactSchema, json["contact_id"])

        self.assertEqual("Luan", contact_schema.name)
        self.assertEqual("99 9999 9999", contact_schema.phone)
