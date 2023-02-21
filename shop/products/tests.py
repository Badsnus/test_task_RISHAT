from django.test import TestCase
from django.shortcuts import reverse

from products.models import Item


class ProductsTests(TestCase):

    def test_get_non_existent_item(self):
        response = self.client.get(reverse('products:item_detail', args=(123123,)))
        self.assertEqual(response.status_code, 404)

    def test_get_item(self):
        created_item = Item.objects.create(name='test_product', description='qwewq', price=123)
        response = self.client.get(reverse('products:item_detail', args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertIn('item', response.context)
        template_item = response.context['item']
        self.assertEqual(created_item, template_item)
        self.assertIn('stripe_public_key', response.context)

    def test_buy_non_existent_item_get(self):
        response = self.client.get(reverse('products:buy_item', args=(123123,)))
        self.assertEqual(response.status_code, 405)

    def test_buy_non_existent_item(self):
        response = self.client.post(reverse('products:buy_item', args=(123123,)))
        self.assertEqual(response.status_code, 404)

    def test_buy_item_get(self):
        Item.objects.create(name='test_product', description='qwewq', price=123)
        response = self.client.get(reverse('products:buy_item', args=(1,)))
        self.assertEqual(response.status_code, 405)

    def test_buy_item(self):
        Item.objects.create(name='test_product', description='qwewq', price=123)
        response = self.client.post(reverse('products:buy_item', args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Content-Type', response.headers)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

    def test_success_and_cancel(self):
        for path in 'success', 'cancel':
            response = self.client.get(reverse(f'products:{path}'))
            self.assertEqual(response.status_code, 200)
