from payment.payment import Payment

class PaymentPix(Payment):
    def process(seld,value):
        print(f"Processando pagamento R${value:.2f} via Pix")