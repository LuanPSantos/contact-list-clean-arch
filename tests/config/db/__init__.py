from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, poolclass=StaticPool, connect_args={"check_same_thread": False}, echo=True, future=True
)


def start_test_session():
    return Session(engine)

