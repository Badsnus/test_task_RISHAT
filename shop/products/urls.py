from django.urls import path

from products.views import ItemDetailView

app_name = 'products'

urlpatterns = [
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail')
]
