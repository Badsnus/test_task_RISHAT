import json

from django.conf import settings
from django.http import JsonResponse
from django.views import generic
from django.shortcuts import get_object_or_404, reverse
from rest_framework import views

from products.models import Item
from products.services import create_payment
from products.utils import CsrfExemptSessionAuthentication


class ItemDetailView(generic.DetailView):
    model = Item
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
        return context


class BuyItemView(views.APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request, *args, **kwargs):
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
