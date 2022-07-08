

class Contact:
    def __init__(self,  name: str, phone: str, user_id: str, contact_id: str | None = None):
        self.contact_id = contact_id
        self.name = name
        self.phone = phone
        self.user_id = user_id

    def __repr__(self):
        return f"Contact(contact_id='{self.contact_id}', name='{self.name}', phone='{self.phone}')"
