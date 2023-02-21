from django.urls import path

from products.views import ItemDetailView, BuyItemView, SuccessView, CancelView

app_name = 'products'

urlpatterns = [
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('buy/<int:pk>/', BuyItemView.as_view(), name='buy_item'),

    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
]
