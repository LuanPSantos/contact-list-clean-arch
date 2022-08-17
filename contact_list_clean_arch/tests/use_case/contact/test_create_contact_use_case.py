from unittest import TestCase
from unittest.mock import patch, MagicMock

from contact_list_clean_arch.app.entity.contact.model.contact import Contact
from contact_list_clean_arch.app.entity.user.model.user import User
from contact_list_clean_arch.app.use_case.contact.create_contact_use_case import CreateContactUseCase, InputModel
from contact_list_clean_arch.tests.util.constants import FIRST
from contact_list_clean_arch.tests.util.mock_path import contact_command_gateway_path, user_query_gateway_path


class TestCreateContactUseCase(TestCase):

    @patch(contact_command_gateway_path)
    @patch(user_query_gateway_path)
    def test_create_contact_successfully(self,
                                         user_query_gateway_mock: MagicMock,
                                         contact_command_gateway_mock: MagicMock):

        user = User(user_id="1", name="Luan", email="Vanda", password="123")
        user_query_gateway_mock.get_by_id.return_value = user

        contact = Contact(contact_id="1", name="Luan", phone="99 9999 9999", user_id="1")
        contact_command_gateway_mock.save.return_value = contact

        use_case = CreateContactUseCase(contact_command_gateway_mock, user_query_gateway_mock)

        output = use_case.execute(InputModel(Contact(name="Luan", phone="99 9999 9999", user_id="1")))

        self.assertEqual(output.contact.contact_id, "1")
        self.assertEqual(output.contact.name, "Luan")
        self.assertEqual(output.contact.phone, "99 9999 9999")

        contact_passed_to_be_saved = contact_command_gateway_mock.save.call_args.args[FIRST]
        contact_command_gateway_mock.save.assert_called_once()

        self.assertEqual(contact_passed_to_be_saved.contact_id, None)
        self.assertEqual(contact_passed_to_be_saved.name, "Luan")
        self.assertEqual(contact_passed_to_be_saved.phone, "99 9999 9999")

        user_query_gateway_mock.get_by_id.assert_called_once_with(user_id="1")
