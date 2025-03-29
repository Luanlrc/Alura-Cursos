from abc import ABC, abstractclassmethod

class Order(ABC):
    def __init__(self, client, itens):
        self.client = client
        self.itens = itens
        self._status = "Criado!"
        self.observers = []

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, new_status):
        self._status = new_status
        self.notification_observers()

    def append_observers(self, observer):
        self.observers.append(observer)

    def notification_observers(self):
        for observer in self.observers:
            observer.update(self)


    @abstractclassmethod
    def calc_total(self):
        pass