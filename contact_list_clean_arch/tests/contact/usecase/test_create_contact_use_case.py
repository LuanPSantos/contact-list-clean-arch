from unittest import TestCase
from unittest.mock import patch

from contact_list_clean_arch.app.contact.model.contact import Contact
from contact_list_clean_arch.app.contact.use_case.create_contact_use_case import CreateContactUseCase, InputModel
from contact_list_clean_arch.tests.util.constants import FIRST
from contact_list_clean_arch.tests.util.mock_path import contact_command_gateway_path


class TestCreateContactUseCase(TestCase):

    def test_create_contact_successfully(self):
        with patch(contact_command_gateway_path) as mock:
            instance = mock.return_value
            instance.save.return_value = Contact(contact_id="1", name="Luan", phone="99 9999 9999")

        use_case = CreateContactUseCase(instance)

        output = use_case.execute(InputModel(Contact(name="Luan", phone="99 9999 9999")))

        self.assertEqual(output.contact.contact_id, "1")
        self.assertEqual(output.contact.name, "Luan")
        self.assertEqual(output.contact.phone, "99 9999 9999")

        contact_passed_to_be_saved = instance.save.call_args.args[FIRST]
        instance.save.assert_called_once_with(contact_passed_to_be_saved)

        self.assertEqual(contact_passed_to_be_saved.contact_id, None)
        self.assertEqual(contact_passed_to_be_saved.name, "Luan")
        self.assertEqual(contact_passed_to_be_saved.phone, "99 9999 9999")
