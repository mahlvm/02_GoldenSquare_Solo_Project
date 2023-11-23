from lib.message import Message
from unittest.mock import Mock

def test_message_true():
    fake_client = Mock()
    message = Message(fake_client)
    fake_client.messages.create.return_value = True
    assert message.send_text("", "") == True


def test_message_false():
    fake_client = Mock()
    message = Message(fake_client)
    fake_client.messages.create.return_value = False
    assert message.send_text("", "") == False