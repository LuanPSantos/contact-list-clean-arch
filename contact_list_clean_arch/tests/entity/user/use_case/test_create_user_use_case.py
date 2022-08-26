from unittest import TestCase
from unittest.mock import patch, MagicMock

from contact_list_clean_arch.app.entity.user.use_case.create_user_use_case import CreateUserUseCase, InputModel
from contact_list_clean_arch.tests.util.constants import ONE
from contact_list_clean_arch.tests.util.mock_path import user_command_gateway_path, cryptography_gateway_path, \
    email_gateway_path
from contact_list_clean_arch.tests.util.teste_factory import create_test_user


class TestCreateUserUseCase(TestCase):

    @patch(email_gateway_path)
    @patch(cryptography_gateway_path)
    @patch(user_command_gateway_path)
    def test_create_user_successfully(self,
                                      user_command_gateway_mock: MagicMock,
                                      cryptography_gateway_mock: MagicMock,
                                      email_gateway_mock: MagicMock):

        user = create_test_user()
        user_command_gateway_mock.create.return_value = user
        cryptography_gateway_mock.hash_password.return_value = user.password

        use_case = CreateUserUseCase(user_command_gateway_mock, cryptography_gateway_mock, email_gateway_mock)

        output = use_case.execute(InputModel(name=user.name, email=user.email, password=user.password))

        self.assertEqual(user.user_id, output.user_id)

        user_passed_to_be_saved = user_command_gateway_mock.create.call_args[ONE]["user"]
        user_command_gateway_mock.create.assert_called_once()

        self.assertEqual(user.name, user_passed_to_be_saved.name)
        self.assertEqual(user.email, user_passed_to_be_saved.email)
        self.assertEqual(user.password, user_passed_to_be_saved.password)

        cryptography_gateway_mock.hash_password.assert_called_once_with(plain_password=user.password)

        user_passed_to_wellcome = email_gateway_mock.send_wellcome_email.call_args[ONE]["user"]
        self.assertEqual(user.name, user_passed_to_wellcome.name)
        self.assertEqual(user.email, user_passed_to_wellcome.email)
        self.assertEqual(user.password, user_passed_to_wellcome.password)
