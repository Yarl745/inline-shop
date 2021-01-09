from asgiref.sync import sync_to_async
from cloudipsp import Api, Checkout, Order

from data.config import FONDY_ID, FONDY_KEY

api = Api(merchant_id=FONDY_ID, secret_key=FONDY_KEY)
checkout = Checkout(api=api)
order = Order(api=api)


@sync_to_async
def get_payment_info(amount, currency="UAH") :
    data = {
        "currency": currency,
        "amount": int(amount*100)
    }
    payment_info = checkout.url(data)
    return payment_info


@sync_to_async
def get_payment_status(order_id: int):
    data = {"order_id": order_id}
    return order.status(data)

