from order.order import Order

class OrderRetirada(Order):
    def calc_total(self):
        return sum(item.value for item in self.itens)