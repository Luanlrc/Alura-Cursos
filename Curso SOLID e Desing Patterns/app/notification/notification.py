from abc import ABC, abstractclassmethod

class Notification(ABC):
    @abstractclassmethod
    def send_notification(self, client, message):
        pass
