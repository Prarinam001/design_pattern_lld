from notificational_channel import NotificationalChannel

## low level class
class EmailService(NotificationalChannel):
    def send(self, message):
        print(f"Sending Email: {message}")