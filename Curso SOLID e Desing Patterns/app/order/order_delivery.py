from order.order import Order

class OrderDelivery(Order):
    def __init__(self, client, itens, taxa_entrega):
        super().__init__(client, itens)
        self.taxa_entrega = taxa_entrega

    def calc_total(self):
        total = sum(item.value for item in self.itens) + self.taxa_entrega
        return total