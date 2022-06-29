import uuid
from unittest import TestCase

import pytest
from fastapi.testclient import TestClient

from contact_list_clean_arch.app.config.db.contact_schema import ContactSchema
from contact_list_clean_arch.app.main import application
from contact_list_clean_arch.tests.config.db import start_local_test_session


class IntegrationTestCase(TestCase):
    @pytest.fixture(autouse=True)
    def run_before_and_after_tests(self):
        print("===> TestGetContactByIdRouter")

        self.__local_session = start_local_test_session()
        print("---- BEFORE TEST ----")
        yield
        print("---- AFTER TEST ----")
        self.__local_session.close()

    def with_local_test_session(self, run):
        self.__local_session.begin()
        print("---- BEGIN TX ----")
        run(self.__local_session)
        print("---- COMMIT TX ----")
        self.__local_session.commit()


class TestGetContactByIdRouter(IntegrationTestCase):
    __httpClient = TestClient(application)

    def test_get_contact_by_id_successfully(self):
        contact_id = str(uuid.uuid4())
        contact_schema = ContactSchema(contact_id=contact_id, name="Lucas", phone="88 8888 8888")

        # TODO get session from parent
        self.with_local_test_session(lambda session: session.add(contact_schema))

        response = self.__httpClient.get(f"/contacts/{contact_id}")

        json = response.json()

        self.assertEqual(200, response.status_code)
        self.assertEqual("Lucas", json["contact"]["name"])
        self.assertEqual("88 8888 8888", json["contact"]["phone"])

    def test_get_contact_by_id_not_found(self):
        contact_id = str(uuid.uuid4())

        response = self.__httpClient.get(f"/contacts/{contact_id}")

        json = response.json()

        self.assertEqual(404, response.status_code)
        self.assertEqual("Contact not found", json["detail"])
