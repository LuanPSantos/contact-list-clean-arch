from sqlalchemy import Column, String

from contact_list_clean_arch.app.config.db import Base


class ContactSchema(Base):
    __tablename__ = 'contact'

    contact_id = Column(String, primary_key=True)
    name = Column(String)
    phone = Column(String)

    def __repr__(self):
        return f"ContactSchema(contact_id='{self.contact_id}', name='{self.name}', phone='{self.phone}')"
