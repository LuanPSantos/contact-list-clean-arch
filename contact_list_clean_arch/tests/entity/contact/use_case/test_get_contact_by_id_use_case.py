from unittest import TestCase
from unittest.mock import patch, MagicMock

from contact_list_clean_arch.app.entity.contact.exception.contact_not_found_exception import ContactNotFoundException
from contact_list_clean_arch.app.entity.contact.model.contact import Contact
from contact_list_clean_arch.app.entity.contact.use_case.get_contact_by_id_use_case import GetContactByIdUseCase, InputModel
from contact_list_clean_arch.tests.util.mock_path import contact_query_gateway_path


class TestGetContactByIdUseCase(TestCase):

    @patch(contact_query_gateway_path)
    def test_get_contact_by_id_successfully(self, contact_query_gateway_mock: MagicMock):

        contact = Contact(contact_id="1", name="Luan", phone="99 9999 9999", user_id="1")
        contact_query_gateway_mock.get_by_id.return_value = contact

        use_case = GetContactByIdUseCase(contact_query_gateway_mock)

        output = use_case.execute(InputModel("1", "1"))

        self.assertEqual(output.contact.contact_id, "1")
        self.assertEqual(output.contact.name, "Luan")
        self.assertEqual(output.contact.phone, "99 9999 9999")

        contact_query_gateway_mock.get_by_id.assert_called_once_with(contact_id="1")

    @patch(contact_query_gateway_path)
    def test_get_contact_by_id_fail(self, contact_query_gateway_mock: MagicMock):
        contact_query_gateway_mock.get_by_id.return_value = None

        use_case = GetContactByIdUseCase(contact_query_gateway_mock)

        self.assertRaises(ContactNotFoundException, use_case.execute, InputModel("1", "1"))

        contact_query_gateway_mock.get_by_id.assert_called_once_with(contact_id="1")
