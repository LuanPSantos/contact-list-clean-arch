from sqlalchemy import create_engine, Column, Integer, String, Sequence, select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class ContactSchema(Base):
    __tablename__ = 'contact'

    contact_id = Column(String, primary_key=True)
    name = Column(String)
    phone = Column(String)


def get_session():
    Session = sessionmaker(bind=engine)

    return Session()
