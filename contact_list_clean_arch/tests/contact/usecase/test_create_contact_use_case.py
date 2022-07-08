from unittest import TestCase
from unittest.mock import patch

from contact_list_clean_arch.app.contact.model.contact import Contact
from contact_list_clean_arch.app.contact.use_case.create_contact_use_case import CreateContactUseCase, InputModel
from contact_list_clean_arch.app.user.model.user import User
from contact_list_clean_arch.tests.util.constants import FIRST
from contact_list_clean_arch.tests.util.mock_path import contact_command_gateway_path, user_query_gateway_path


class TestCreateContactUseCase(TestCase):

    def test_create_contact_successfully(self):
        with patch(user_query_gateway_path) as user_query_gateway_mock:
            user_query_gateway = user_query_gateway_mock.return_value
            user_query_gateway.save.return_value = User(user_id="1", name="Luan", email="Vanda", password="123")
        with patch(contact_command_gateway_path) as contact_command_gateway_mock:
            contact_command_gateway = contact_command_gateway_mock.return_value
            contact_command_gateway.save.return_value = Contact(contact_id="1", name="Luan", phone="99 9999 9999", user_id="1")

        use_case = CreateContactUseCase(contact_command_gateway, user_query_gateway)

        output = use_case.execute(InputModel(Contact(name="Luan", phone="99 9999 9999", user_id="1")))

        self.assertEqual(output.contact.contact_id, "1")
        self.assertEqual(output.contact.name, "Luan")
        self.assertEqual(output.contact.phone, "99 9999 9999")

        contact_passed_to_be_saved = contact_command_gateway.save.call_args.args[FIRST]
        contact_command_gateway.save.assert_called_once()

        self.assertEqual(contact_passed_to_be_saved.contact_id, None)
        self.assertEqual(contact_passed_to_be_saved.name, "Luan")
        self.assertEqual(contact_passed_to_be_saved.phone, "99 9999 9999")
