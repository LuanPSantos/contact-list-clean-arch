from unittest import TestCase
from unittest.mock import patch

from contact_list_clean_arch.app.domain.auth.exception.unauthenticated_exception import UnauthenticatedException
from contact_list_clean_arch.app.domain.auth.use_case.user_authentication_use_case import UserAuthenticationUseCase, \
    InputModel
from contact_list_clean_arch.tests.util.constants import AUTHORIZATION_TOKEN
from contact_list_clean_arch.tests.util.mock_path import user_query_gateway_path, cryptography_gateway_path, \
    authorization_token_gateway_path
from contact_list_clean_arch.tests.util.teste_factory import create_test_user


class TestUserAuthenticationUseCase(TestCase):

    @patch(authorization_token_gateway_path)
    @patch(cryptography_gateway_path)
    @patch(user_query_gateway_path)
    def test_authenticate_user_successfully(self,
                                            user_query_gateway_mock,
                                            cryptography_gateway_mock,
                                            authorization_token_gateway_mock):
        user = create_test_user()
        user_query_gateway_mock.get_by_email.return_value = user
        cryptography_gateway_mock.match_password.return_value = True
        authorization_token_gateway_mock.create_token.return_value = AUTHORIZATION_TOKEN

        use_case = UserAuthenticationUseCase(
            user_query_gateway_mock, cryptography_gateway_mock, authorization_token_gateway_mock
        )

        output = use_case.execute(InputModel(email=user.email, password=user.password))

        self.assertEqual(AUTHORIZATION_TOKEN, output.authorization_token)

        user_query_gateway_mock.get_by_email.assert_called_once_with(email=user.email)
        cryptography_gateway_mock.match_password.assert_called_once_with(
            plain_password=user.password,
            hashed_password=user.password
        )
        authorization_token_gateway_mock.create_token.assert_called_once_with(user_id=user.user_id)

    @patch(authorization_token_gateway_path)
    @patch(cryptography_gateway_path)
    @patch(user_query_gateway_path)
    def test_authenticate_user_not_found(self,
                                         user_query_gateway_mock,
                                         cryptography_gateway_mock,
                                         authorization_token_gateway_mock):
        user = create_test_user()
        user_query_gateway_mock.get_by_email.return_value = None

        use_case = UserAuthenticationUseCase(
            user_query_gateway_mock, cryptography_gateway_mock, authorization_token_gateway_mock
        )

        self.assertRaises(UnauthenticatedException,
                          use_case.execute, InputModel(email=user.email, password=user.password))

        user_query_gateway_mock.get_by_email.assert_called_once_with(email=user.email)
        cryptography_gateway_mock.match_password.assert_not_called()
        authorization_token_gateway_mock.create_token.assert_not_called()

    @patch(authorization_token_gateway_path)
    @patch(cryptography_gateway_path)
    @patch(user_query_gateway_path)
    def test_authenticate_passwords_not_match(self,
                                              user_query_gateway_mock,
                                              cryptography_gateway_mock,
                                              authorization_token_gateway_mock):
        user = create_test_user()
        user_query_gateway_mock.get_by_email.return_value = user
        cryptography_gateway_mock.match_password.return_value = False

        use_case = UserAuthenticationUseCase(
            user_query_gateway_mock, cryptography_gateway_mock, authorization_token_gateway_mock
        )

        self.assertRaises(UnauthenticatedException,
                          use_case.execute, InputModel(email=user.email, password=user.password))

        user_query_gateway_mock.get_by_email.assert_called_once_with(email=user.email)
        cryptography_gateway_mock.match_password.assert_called_once_with(
            plain_password=user.password,
            hashed_password=user.password
        )
        authorization_token_gateway_mock.create_token.assert_not_called()
