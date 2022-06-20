from unittest import TestCase

from fastapi.testclient import TestClient

from contact_list_clean_arch.main import application


class TestGetContactByIdRouter(TestCase):
    __httpClient = TestClient(application)

    def test_create_contact_successfully(self):
        response = self.__httpClient.post("/contacts", json={"name": "Luan", "phone": "99 9999 9999"})

        self.assertEqual(response.json(), {"contact_id": 1})
        self.assertEqual(response.status_code, 201)
