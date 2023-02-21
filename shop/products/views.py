from django.views import generic

from products.models import Item


class ItemDetailView(generic.DetailView):
    model = Item
    context_object_name = 'item'
