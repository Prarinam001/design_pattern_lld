from notificational_channel import NotificationalChannel

class NotificaationService:
    def __init__(self, channel: NotificationalChannel):
        self.channel = channel

    def notify(self, message):
        self.channel.send(message)