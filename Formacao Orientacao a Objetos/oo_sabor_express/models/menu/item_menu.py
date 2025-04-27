from abc import ABC


class ItemMenu(ABC):
    def __init__(self, name, value):
        self._name = name
        self._value = value

    @classmethod
    def apply_discount(self):
        pass
