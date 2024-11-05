from django.test import TestCase 
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(id=10,title="IceCream", price=5, inventory=100)
        self.assertEqual(item.dish, "IceCream")
        self.assertEqual(item.price, 80)
    