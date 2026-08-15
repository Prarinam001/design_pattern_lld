from sms_service import SMSService
from email_service import EmailService
from notification_service import NotificaationService

sms_service = SMSService()

ns = NotificaationService(sms_service)
ns.notify("hey")