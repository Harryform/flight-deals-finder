from twilio.rest import Client

ACCOUNT_SID = YOUR_SID
AUTH_TOKEN = YOUR_TOKEN
VIRTUAL_NUMBER = YOUR_NUMBER
PHONE_NUMBER = YOUR_PHONE


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
