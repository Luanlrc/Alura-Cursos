
from notification.notification import Notification

class NotificationSms(Notification):
    def send_notification(self, client, message):
        print(f"Enviando sms para o cliente {client.name}: \n{message}")
