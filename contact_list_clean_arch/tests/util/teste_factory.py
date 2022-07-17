import uuid
from random import randint

from contact_list_clean_arch.app.domain.contact.model.contact import Contact
from contact_list_clean_arch.app.domain.user.model.user import User
from contact_list_clean_arch.tests.util.constants import PLAIN_PASSWORD


def create_test_user() -> User:
    random = f"{uuid.uuid4()}"[-12:]
    user_id = str(uuid.uuid4())
    name = str(f"Name {random} da Silva")
    email = str(f"email.{random}@test.com")
    password = PLAIN_PASSWORD

    return User(name, email, password, user_id)


def create_test_contact(user_id: str) -> Contact:
    random = f"{uuid.uuid4()}"[-12:]
    name = str(f"Name {random} da Silva")
    phone = str(f"({randint(10, 99)}) {randint(10000, 99999)}-{randint(1000, 9999)}")

    return Contact(name, phone, user_id)
