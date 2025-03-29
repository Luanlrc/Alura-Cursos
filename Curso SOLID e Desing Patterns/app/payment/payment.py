from abc import ABC, abstractclassmethod

class Payment(ABC):
    @abstractclassmethod
    def process(self, value):
        pass