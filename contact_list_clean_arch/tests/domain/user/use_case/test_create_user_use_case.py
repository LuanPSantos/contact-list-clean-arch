from unittest import TestCase
from unittest.mock import patch, MagicMock
from contact_list_clean_arch.app.domain.user.use_case.create_user_use_case import CreateUserUseCase, InputModel
from contact_list_clean_arch.tests.util.constants import FIRST
from contact_list_clean_arch.tests.util.mock_path import user_command_gateway_path, cryptography_gateway_path
from contact_list_clean_arch.tests.util.teste_factory import create_test_user


class TestCreateUserUseCase(TestCase):

    @patch(cryptography_gateway_path)
    @patch(user_command_gateway_path)
    def test_create_user_successfully(self, user_command_gateway_mock: MagicMock, cryptography_gateway_mock: MagicMock):

        user = create_test_user()
        user_command_gateway_mock.create.return_value = user

        cryptography_gateway_mock.hash_password.return_value = "encrypted_password"

        use_case = CreateUserUseCase(user_command_gateway_mock, cryptography_gateway_mock)

        output = use_case.execute(InputModel(name=user.name, email=user.email, password=user.password))

        self.assertEqual(user.user_id, output.user_id)

        user_passed_to_be_saved = user_command_gateway_mock.create.call_args.args[FIRST]
        user_command_gateway_mock.create.assert_called_once()

        self.assertEqual(user.name, user_passed_to_be_saved.name)
        self.assertEqual(user.email, user_passed_to_be_saved.email)
        self.assertEqual("encrypted_password", user_passed_to_be_saved.password)

        cryptography_gateway_mock.hash_password.assert_called_once_with(user.password)
