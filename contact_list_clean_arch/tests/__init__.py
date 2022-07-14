from fastapi.security import HTTPBearer
from starlette.requests import Request

from contact_list_clean_arch.app import Base
from contact_list_clean_arch.app.config.db import start_session
from contact_list_clean_arch.app.main import application
from contact_list_clean_arch.tests.config.db import start_test_session, engine


class JWTBearerTestMiddleware(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearerTestMiddleware, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        return True


application.dependency_overrides[start_session] = start_test_session
Base.metadata.create_all(engine)
