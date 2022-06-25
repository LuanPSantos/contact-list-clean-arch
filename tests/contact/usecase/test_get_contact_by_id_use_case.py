from unittest import TestCase
from unittest.mock import patch

from contact_list_clean_arch.contact.exception.contact_not_found_exception import ContactNotFoundException
from contact_list_clean_arch.contact.model.contact import Contact
from contact_list_clean_arch.contact.use_case.get_contact_by_id_use_case import GetContactByIdUseCase, InputModel
from tests.util.mock_path import contact_query_gateway_path


class TestGetContactByIdUseCase(TestCase):

    def test_get_contact_by_id_successfully(self):
        with patch(contact_query_gateway_path) as mock:
            instance = mock.return_value
            instance.get_by_id.return_value = Contact(contact_id="1", name="Luan", phone="99 9999 9999")

        use_case = GetContactByIdUseCase(instance)

        output = use_case.execute(InputModel("1"))

        self.assertEqual(output.contact.contact_id, "1")
        self.assertEqual(output.contact.name, "Luan")
        self.assertEqual(output.contact.phone, "99 9999 9999")

        instance.get_by_id.assert_called_once()

    def test_get_contact_by_id_fail(self):
        with patch(contact_query_gateway_path) as mock:
            instance = mock.return_value
            instance.get_by_id.return_value = None

        use_case = GetContactByIdUseCase(instance)

        self.assertRaises(ContactNotFoundException, use_case.execute, InputModel("1"))

        instance.get_by_id.assert_called_once_with("1")
