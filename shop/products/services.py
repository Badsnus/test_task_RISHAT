import stripe
from django.conf import settings

from products.models import Item


def create_payment(item: Item, success_url, cancel_url) -> dict:
    session = stripe.checkout.Session.create(
        settings.STRIPE_SECRET_KEY,
        line_items=[{
            'price_data': {
                'currency': item.currency,
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
    )

    return {'session_id': session['id']}
