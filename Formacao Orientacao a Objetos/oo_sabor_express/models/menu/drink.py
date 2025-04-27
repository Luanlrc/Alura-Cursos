from models.menu.item_menu import ItemMenu


class Drink(ItemMenu):
    def __init__(self, name, value, size):
        super().__init__(name, value)
        self.size = size

    def __str__(self) -> str:
        return self._name

    def apply_discount(self):
        self._value -= self._value * 0.08
