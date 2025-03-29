from client import Client
from item import Item
from order.order_delivery import OrderDelivery
from payment.payment_factory import PagamentoFactory
from notification.notification_facade import NotificationFacade
from observer.status_observer import ObserverStatus

client = Client("Luan", "Alura")
item_one = Item("Pizza", 30.00)
item_two = Item("Refri", 5.00)
itens = [item_one, item_two]

taxa_entrega = 10.0
order = OrderDelivery(client, itens, taxa_entrega)

order_value = order.calc_total()
type_payment = "pix"
payment = PagamentoFactory.create_payment(type_payment)
payment.process(order_value)

MESSAGE_PAID = "O pagamento foi confirmado!"
MESSAGE_PREAPARING = "O pedido esta sendo preparado!"
MESSAGE_SENT = "O pedido saiu para a Entrega!"

notifications = NotificationFacade()
observer = ObserverStatus(notifications)
order.append_observers(observer)

order.status = MESSAGE_PAID
order.status = MESSAGE_PREAPARING
order.status = MESSAGE_SENT