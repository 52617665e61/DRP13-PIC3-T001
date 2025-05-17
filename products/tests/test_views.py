from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class ProductViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser(from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class ProductViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser(
            email='admin@test.com',
            user_name='admin',
            first_name='Admin',
            last_name='User',
            password='adminpass'
        )
        self.product = Product.objects.create(
            name='Filtro Teste',
            category='Filtro',
            value=100,
            description='Teste view'
        )

    def test_products_list_view_

            username='admin',
            email='admin@test.com',
            password='adminpass'
        )
        self.product = Product.objects.create(
            name='Filtro Teste', category='Filtro', value=100, description='Teste view'
        )

    def test_products_list_view(self):
        response = self.client.get('/productsList')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Filtro Teste')

    def test_superuser_can_add_product(self):
        self.client.login(username='admin', password='adminpass')
        form_data = {
            'name': 'Novo Produto',
            'category': 'Cabo',
            'value': 321,
            'description': 'Descrição',
        }
        response = self.client.post('/addProduct', data=form_data)
        self.assertEqual(response.status_code, 302)

    def test_update_product(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post(f'/updateProduct/{self.product.id}', {
            'name': 'Atualizado',
            'category': 'Filtro',
            'value': 123,
            'description': 'Atualizado'
        })
        self.assertEqual(response.status_code, 302)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Atualizado')

    def test_delete_product(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(f'/delProduct/{self.product.id}')
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())

