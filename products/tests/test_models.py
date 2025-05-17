from django.test import TestCase
from products.models import Product
from django.core.exceptions import ValidationError

class ProductModelTest(TestCase):
    def test_str_representation(self):
        product = Product(name='Produto A', category='Filtro', value=10.0, description='Desc')
        self.assertEqual(str(product), 'Produto A')

    def test_field_max_lengths(self):
        product = Product(
            name='x' * 50,
            category='Filtro',
            value=10.0,
            description='y' * 500
        )
        try:
            product.full_clean()  # não deve levantar erro
        except ValidationError:
            self.fail("full_clean() levantou erro com campos no limite de tamanho")

    def test_negative_value_should_fail(self):
        product = Product(
            name='Produto Inválido',
            category='Filtro',
            value=-5.0,
            description='Valor negativo'
        )
        with self.assertRaises(ValidationError):
            product.full_clean()
