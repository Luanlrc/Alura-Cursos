from notification.notification import Notification

class NotificationEmail(Notification):
    def send_notification(self, client, message):
        print(f"Enviando email para o cliente {client.name}: \n{message}")
