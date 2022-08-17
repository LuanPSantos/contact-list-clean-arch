from sqlalchemy import Column, String, ForeignKey

from contact_list_clean_arch.app.infrastructure.config.db.db_setup import Base


class ContactSchema(Base):
    __tablename__ = 'contact'

    contact_id = Column(String, primary_key=True)
    name = Column(String)
    phone = Column(String)
    user_id = Column(String, ForeignKey('user.user_id'))

    def __repr__(self):
        return f"ContactSchema(contact_id='{self.contact_id}', name='{self.name}', phone='{self.phone}')"
