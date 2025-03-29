from payment.payment import Payment

class PaymentCard(Payment):
    def process(seld,value):
        print(f"Processando pagamento R${value:.2f} via Cartão")