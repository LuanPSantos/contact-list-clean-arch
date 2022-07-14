from unittest import TestCase
from unittest.mock import patch

from contact_list_clean_arch.app.user.model.user import User
from contact_list_clean_arch.app.user.use_case.create_user_use_case import CreateUserUseCase, InputModel
from contact_list_clean_arch.tests.util.constants import FIRST
from contact_list_clean_arch.tests.util.mock_path import user_command_gateway_path, cryptography_gateway_path


class TestCreateUserUseCase(TestCase):

    def test_create_user_successfully(self):
        with patch(user_command_gateway_path) as user_command_gateway_mock:
            user_command_gateway = user_command_gateway_mock.return_value

            user = User(user_id="1", name="Maria", email="maria@email.com", password="123")
            user_command_gateway.create.return_value = user

        with patch(cryptography_gateway_path) as cryptography_gateway_mock:
            cryptography_gateway = cryptography_gateway_mock.return_value

            cryptography_gateway.hash_password.return_value = "encrypted_password"

        use_case = CreateUserUseCase(user_command_gateway, cryptography_gateway)

        output = use_case.execute(InputModel(name="Maria", email="maria@email.com", password="123"))

        self.assertEqual("1", output.user_id)

        user_passed_to_be_saved = user_command_gateway.create.call_args.args[FIRST]
        user_command_gateway.create.assert_called_once()

        self.assertEqual("Maria", user_passed_to_be_saved.name)
        self.assertEqual("maria@email.com", user_passed_to_be_saved.email)
        self.assertEqual("encrypted_password", user_passed_to_be_saved.password)

        cryptography_gateway.hash_password.assert_called_once_with("123")
