from contact_list_clean_arch.app import Base
from contact_list_clean_arch.app.config.db import start_session
from contact_list_clean_arch.app.main import application
from contact_list_clean_arch.tests.config.db import start_test_session, engine

application.dependency_overrides[start_session] = start_test_session
Base.metadata.create_all(engine)
