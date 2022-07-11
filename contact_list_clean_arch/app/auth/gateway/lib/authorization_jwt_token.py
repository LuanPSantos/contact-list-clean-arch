from datetime import timedelta, datetime

from jose import jwt

from contact_list_clean_arch.app.auth.gateway.authorization_token_gateway import AuthorizationTokenGateway
from contact_list_clean_arch.app.config.security.security_config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, \
    ALGORITHM


class AuthorizationJwtTokenGateway(AuthorizationTokenGateway):
    def create_token(self, user_id) -> str:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        if access_token_expires:
            expire = datetime.utcnow() + access_token_expires
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)

        to_encode = {
            "exp": expire,
            "sub": user_id
        }

        jwt_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

        return jwt_token
