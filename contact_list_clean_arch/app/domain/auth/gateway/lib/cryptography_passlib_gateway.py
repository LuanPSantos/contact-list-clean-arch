from fastapi import Depends
from passlib.context import CryptContext

from contact_list_clean_arch.app.config.security.security_config import get_crypt_context
from contact_list_clean_arch.app.domain.auth.gateway.cryptography_gateway import CryptographyGateway


class CryptographyPasslibGateway(CryptographyGateway):
    def __init__(self, crypt_context: CryptContext = Depends(get_crypt_context)):
        self.crypt_context = crypt_context

    def match_password(self, plain_password, hashed_password) -> bool:
        return self.crypt_context.verify(plain_password, hashed_password)

    def hash_password(self, plain_password: str) -> str:
        return self.crypt_context.hash(plain_password)
