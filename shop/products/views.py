import json

from django.views import generic
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, reverse
from rest_framework.views import APIView
import stripe

from products.models import Item


class ItemDetailView(generic.DetailView):
    model = Item
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
        return context


class BuyItemView(APIView):

    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        item = get_object_or_404(Item, pk=kwargs.get('pk'))
        # payment = stripe.PaymentIntent.create(
        #     amount=item.price * 100,
        #     currency='usd',
        # )
        # print(payment)

        session = stripe.checkout.Session.create(
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
            success_url=settings.SITE_DOMAIN + reverse('products:success'),
            cancel_url=settings.SITE_DOMAIN + reverse('products:cancel'),
            # payment_intent_data=payment.client_secret,
            # line_items=[
            #     {
            #         'payment_intent': ,
            #         'quantity': 1,
            #     },
            # ],
        )

        return JsonResponse(json.dumps({'session_id': session['id']}), safe=False)


class SuccessView(generic.TemplateView):
    template_name = 'products/success.html'


class CancelView(generic.TemplateView):
    template_name = 'products/cancel.html'
