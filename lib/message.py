#import os
#from twilio.rest import Client

#account_sid = os.environ["ACaa7554b36291e68ab3a4e682de7bd620"]
#auth_token = os.environ["c8e15d074d8a08133de7c3fb3f1b4a28"]
#client = Client(account_sid, auth_token)

class Message:
    def __init__(self, client):
        self.client = client

    def send_text(self, phone, message):
        message = self.client.messages \
            .create(
                    body = message, 
                    from_= "+4407506287291",
                    to = phone
                )
        return message