from fastapi import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt

from contact_list_clean_arch.app.config.security.security_config import SECRET_KEY, ALGORITHM
from contact_list_clean_arch.app.domain.auth.exception.unauthorized_exception import UnauthorizedException


def verify_jwt(jwt_token: str):
    try:
        jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub")
    except Exception:
        raise UnauthorizedException()


class JWTBearerMiddleware(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearerMiddleware, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearerMiddleware, self).__call__(request)
        if credentials and credentials.scheme == "Bearer":
            verify_jwt(credentials.credentials)
        else:
            raise UnauthorizedException()

