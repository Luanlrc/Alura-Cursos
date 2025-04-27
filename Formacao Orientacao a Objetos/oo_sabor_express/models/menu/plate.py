from models.menu.item_menu import ItemMenu


class Plate(ItemMenu):
    def __init__(self, name, value, description):
        super().__init__(name, value)
        self.description = description

    def __str__(self) -> str:
        return self._name

    def apply_discount(self):
        self._value -= self._value * 0.05
