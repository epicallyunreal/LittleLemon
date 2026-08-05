from django.test import TestCase

class MenuTestCase(TestCase):
    def test_menu_item_creation(self):
        from restaurant.models import Menu
        menu_item = Menu.objects.create(Title='Ice Cream', Price=20, Inventory=5)
        self.assertEqual(menu_item.Title, 'Ice Cream')
        self.assertEqual(menu_item.Price, 20)
        self.assertEqual(menu_item.Inventory, 5)

class MenuViewTestCase(TestCase):

    def setUp(self):
        from restaurant.models import Menu
        Menu.objects.create(Title='Ice Cream', Price=20, Inventory=5)
        Menu.objects.create(Title='Pizza', Price=15, Inventory=10)
        Menu.objects.create(Title='Burger', Price=10, Inventory=8)

    def test_getall(self):
        from restaurant.models import Menu
        menu_items = Menu.objects.all()
        self.assertEqual(menu_items.count(), 3)

    def test_menu_view(self):
        from restaurant.models import Menu
        from django.urls import reverse
        menu_item1 = Menu.objects.create(Title='Ice Cream', Price=20, Inventory=5)
        menu_item2 = Menu.objects.create(Title='Pizza', Price=15, Inventory=10)
        menu_item3 = Menu.objects.create(Title='Burger', Price=10, Inventory=8)
        response = self.client.get(reverse('menu-items'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ice Cream')
        self.assertContains(response, 'Pizza')
        self.assertContains(response, 'Burger')