from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt

from contact_list_clean_arch.app.config.security.security_config import SECRET_KEY, ALGORITHM


def verify_jwt(jwt_token: str):
    try:
        jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub")
    except Exception:
        raise HTTPException(status_code=403, detail="Unauthorized")


class JWTBearerMiddleware(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearerMiddleware, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearerMiddleware, self).__call__(request)
        if credentials and credentials.scheme == "Bearer":
            verify_jwt(credentials.credentials)
        else:
            raise HTTPException(status_code=403, detail="Unauthorized")

