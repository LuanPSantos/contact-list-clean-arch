from sqlalchemy import Column, String

from contact_list_clean_arch.app.infrastructure.config.db.db_setup import Base


class UserSchema(Base):
    __tablename__ = 'user'

    user_id = Column(String, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return f"UserSchema(user_id='{self.user_id}', name='{self.name}', email='{self.email}')"
