class ObserverStatus:
    def __init__(self, notifications):
        self.notifications = notifications

    def update (self, order):
        message = f"O pedido foi atualizado para {order.status}"
        self.notifications.send_notifications(order.client, message)