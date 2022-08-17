from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, poolclass=StaticPool, connect_args={"check_same_thread": False}, echo=True, future=True
)


def start_test_session():
    db = Session(engine)
    print("init-session")
    try:
        print("before-session-use")
        yield db
        db.commit()
        print("after-session-use")
    except Exception:
        print("session-rollback")
        db.rollback()
    finally:
        print("session-ends")
        db.close()


def start_local_test_session():
    return Session(engine)
