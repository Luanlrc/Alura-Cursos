from notification.notification_email import NotificationEmail
from notification.notification_sms import NotificationSms

class NotificationFacade:
    def __init__(self):
        self.notifications = [NotificationEmail(), NotificationSms()]

    def send_notifications(self, client, message):
        for notification in self.notifications:
            notification.send_notification(client, message)
