from django.test import TestCase, Client
from django.urls import reverse

from .models import Menu, Item, Ingredient

client = Client()


class ModelsTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(season='summer')
        Item.objects.create(name='Nuka Cola', chef_id=0,)
        Ingredient.objects.create(name='Plutonium')

    def test_menu(self):
        menu = Menu.objects.get(season='summer')
        self.assertEqual(str(menu), 'summer')

    def test_item(self):
        item = Item.objects.get(name='Nuka Cola')
        self.assertEqual(item.chef_id, 0)
        self.assertEqual(str(item), 'Nuka Cola')

    def test_ingredient(self):
        ingredient = Ingredient.objects.get(name='Plutonium')
        self.assertEqual(str(ingredient), 'Plutonium')


class ViewsTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(season='Fall')
        Item.objects.create(name='Jolt Cola', chef_id=0,)
        Ingredient.objects.create(name='caffeine')

    def test_menu_list(self):
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_menu_detail(self):
        response = client.get('/menu/1/')
        self.assertEqual(response.status_code, 200)

    def test_edit_menu(self):
        response = client.get('/menu/1/edit/')
        self.assertEqual(response.status_code, 200)
        with self.assertRaises(ValueError):
            # error request
            response = client.post(
                '/menu/1/edit/',
                {'season': 'Summer',
                    'expiration_date_month': '13',
                    'expiration_date_day': '41',
                    'expiration_date_year': '2020',
                    'items': "1"})
        # valid request
        response = client.post(
            '/menu/1/edit/',
            {'season': 'Summer',
                'expiration_date_month': '1',
                'expiration_date_day': '1',
                'expiration_date_year': '2020',
                'items': "1"})
        self.assertEqual(response.status_code, 302)

    def test_item_detail(self):
        response = client.get('/menu/item/1/')
        self.assertEqual(response.status_code, 200)

    def test_create_new_menu(self):
        response = client.get('/menu/new/')
        # error request
        response = client.post(
            '/menu/new/',
            {'season': 'Summer',
                'expiration_date_month': '1',
                'expiration_date_day': '1',
                'expiration_date_year': '2020',
                'items': "1"})
        # valid request
        response = client.post(
            '/menu/new/',
            {'season': 'Summer',
                'expiration_date_month': '13',
                'expiration_date_day': '41',
                'expiration_date_year': '2020',
                'items': "1"})
        self.assertEqual(response.status_code, 200)
