#import os
#from twilio.rest import Client

#account_sid = os.environ["###"]
#auth_token = os.environ["###]
#client = Client(account_sid, auth_token)

class Message:
    def __init__(self, client):
        self.client = client

    def send_text(self, phone, message):
        message = self.client.messages \
            .create(
                    body = message, 
                    from_= "+440########",
                    to = phone
                )
        return message