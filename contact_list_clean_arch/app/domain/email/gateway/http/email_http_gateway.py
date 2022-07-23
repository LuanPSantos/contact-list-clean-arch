import json

import requests

from contact_list_clean_arch.app.domain.email.gateway.email_gateway import EmailGateway
from contact_list_clean_arch.app.domain.user.model.user import User

EMAIL_SERVICE_URL = "http://localhost:8080"


class EmailHttpGateway(EmailGateway):

    def send_wellcome_email(self, user: User) -> None:
        response = requests.post(url=f"{EMAIL_SERVICE_URL}/emails/wellcome",
                                 data=json.dumps({"user_name": user.name, "user_email": user.email}),
                                 headers={"Content-Type": "application/json"})

        response.raise_for_status()
