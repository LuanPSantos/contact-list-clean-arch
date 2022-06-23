from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.pool import StaticPool

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, poolclass=StaticPool, connect_args={"check_same_thread": False}, echo=True, future=True
)

Base = declarative_base()


def start_session():
    #return None
    return Session(engine)
