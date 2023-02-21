import json

from django.views import generic
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, reverse
from rest_framework.views import APIView

from products.models import Item
from products.services import create_payment


class ItemDetailView(generic.DetailView):
    model = Item
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
        return context


class BuyItemView(APIView):

    def post(self, request, *args, **kwargs):
        # payment = stripe.PaymentIntent.create(
        #     amount=item.price * 100,
        #     currency='usd',
        # )
        # print(payment)
        session_id = create_payment(
            get_object_or_404(Item, pk=kwargs.get('pk')),
            settings.SITE_DOMAIN + reverse('products:success'),
            settings.SITE_DOMAIN + reverse('products:cancel'),
        )

        return JsonResponse(json.dumps(session_id), safe=False)


class SuccessView(generic.TemplateView):
    template_name = 'products/success.html'


class CancelView(generic.TemplateView):
    template_name = 'products/cancel.html'
