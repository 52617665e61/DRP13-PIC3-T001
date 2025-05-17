from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class PermissionTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email='user@test.com',
            user_name='user',
            first_name='Regular',
            last_name='User',
            password2='userpass'
        )
        self.product = Product.objects.create(
            name='Produto Público',
            category='Cabo',
            value=10.0,
            description='Produto para teste'
        )

    def test_normal_user_cannot_access_add_product(self):
        self.client.login(username='user', password='userpass')
        response = self.client.get('/addProduct')
        self.assertEqual(response.status_code, 302)  # redirecionado

    def test_normal_user_cannot_delete_product(self):
        self.client.login(username='user', password='userpass')
        response = self.client.get(f'/delProduct/{self.product.id}')
        self.assertEqual(response.status_code, 302)
