from unittest import TestCase
from unittest.mock import patch, MagicMock

from contact_list_clean_arch.app.domain.user.exception.user_not_fount_exception import UserNotFoundException
from contact_list_clean_arch.app.domain.user.model.user import User
from contact_list_clean_arch.app.domain.user.use_case import GetUserByIdUseCase, InputModel
from contact_list_clean_arch.tests.util.mock_path import user_query_gateway_path


class TestGetUserByIdUseCase(TestCase):

    @patch(user_query_gateway_path)
    def test_get_user_by_id_successfully(self, user_query_gateway_mock: MagicMock):

        user = User(user_id="1", name="Marcos", email="marcos@email.com", password="123")
        user_query_gateway_mock.get_by_id.return_value = user

        use_case = GetUserByIdUseCase(user_query_gateway_mock)

        output = use_case.execute(InputModel(user_id="1"))

        self.assertEqual("1", output.user.user_id)
        self.assertEqual("Marcos", output.user.name)
        self.assertEqual("marcos@email.com", output.user.email)
        self.assertEqual("123", output.user.password)

        user_query_gateway_mock.get_by_id.assert_called_once_with(user_id="1")

    @patch(user_query_gateway_path)
    def test_get_user_by_id_failed_due_not_found(self, user_query_gateway_mock):

        user_query_gateway_mock.get_by_id.return_value = None

        use_case = GetUserByIdUseCase(user_query_gateway_mock)

        self.assertRaises(UserNotFoundException, use_case.execute, InputModel(user_id="1"))

        user_query_gateway_mock.get_by_id.assert_called_once_with(user_id="1")
