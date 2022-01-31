from twilio.rest import Client

ACCOUNT_SID = "ACbea4ffd4267f5af210bf02f4be2c4f0e"
AUTH_TOKEN = "3203f2eda57a2fb25dc9c2bd3dc39a82"
VIRTUAL_NUMBER = "+12694431987"
PHONE_NUMBER = "+15403706668"


class NotificationManager:

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages \
            .create(
            body=message,
            from_=VIRTUAL_NUMBER,
            to=PHONE_NUMBER,
            )

        print(message.sid)
