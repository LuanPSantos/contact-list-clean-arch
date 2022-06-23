from sqlalchemy import Column, String

from contact_list_clean_arch.config.db.db_config import Base


class ContactSchema(Base):
    __tablename__ = 'contact'

    contact_id = Column(String, primary_key=True)
    name = Column(String)
    phone = Column(String)
