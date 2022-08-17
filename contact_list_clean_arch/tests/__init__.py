from contact_list_clean_arch.app.infrastructure.config.db.db_setup import start_session, Base
from contact_list_clean_arch.app.main import application
from contact_list_clean_arch.tests.infrastructure.config.db.db_setup import start_test_session, engine

application.dependency_overrides[start_session] = start_test_session
Base.metadata.create_all(engine)
