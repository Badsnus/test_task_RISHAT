import stripe
from django.conf import settings

from products.models import Item


def create_payment(item: Item, success_url, cancel_url) -> dict:
    session = stripe.checkout.Session.create(
        settings.STRIPE_SECRET_KEY,
        line_items=[{
            'price_data': {
                'currency': 'USD',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price * 100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=success_url,
        cancel_url=cancel_url,
        # payment_intent_data=payment.client_secret,
        # line_items=[
        #     {
        #         'payment_intent': ,
        #         'quantity': 1,
        #     },
        # ],
    )
    return {'session_id': session['id']}
