from payment.payment_card import PaymentCard
from payment.payment_pix import PaymentPix

class PagamentoFactory:
    @staticmethod
    def create_payment(type):
        if type == "pix":
            return PaymentPix()
        elif type == "card":
            return PaymentCard()
        else:
            raise ValueError(f"Tipo de pagamento '{type}' não suportado")