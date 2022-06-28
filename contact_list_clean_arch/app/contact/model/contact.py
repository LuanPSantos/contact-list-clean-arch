

class Contact:
    def __init__(self,  name: str, phone: str, contact_id: str | None = None):
        self.contact_id = contact_id
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"Contact(contact_id='{self.contact_id}', name='{self.name}', phone='{self.phone}')"
