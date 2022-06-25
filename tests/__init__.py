from contact_list_clean_arch import Base
from contact_list_clean_arch.config.db import start_session
from contact_list_clean_arch.main import application
from tests.config.db import start_test_session, engine

application.dependency_overrides[start_session] = start_test_session
Base.metadata.create_all(engine)
