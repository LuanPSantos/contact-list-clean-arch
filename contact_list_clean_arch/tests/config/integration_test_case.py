import pytest

from contact_list_clean_arch.app.main import application
from contact_list_clean_arch.tests.config.db import start_local_test_session
from unittest import TestCase
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


class IntegrationTestCase(TestCase):
    _local_session: Session
    _httpClient = TestClient(application)

    @pytest.fixture(autouse=True)
    def run_before_and_after_tests(self):

        self._local_session = start_local_test_session()
        print("---- BEFORE TEST ----")
        yield
        print("---- AFTER TEST ----")
        self._local_session.close()
