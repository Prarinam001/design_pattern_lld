from notificational_channel import NotificationalChannel

## low level class
class SMSService(NotificationalChannel):
    def send(self, message):
        print(f"Sending SMS: {message}")