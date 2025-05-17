from django.test import TestCase
from products.form import ProductForm
from django.core.files.uploadedfile import SimpleUploadedFile

class ProductFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'name': 'Produto X',
            'category': 'Filtro',
            'value': 123.45,
            'description': 'Descrição'
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_negative_value(self):
        form_data = {
            'name': 'Produto Negativo',
            'category': 'Filtro',
            'value': -50,
            'description': 'Erro de valor'
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_image_upload(self):
        image = SimpleUploadedFile("test.jpg", b"img content", content_type="image/jpeg")
        form_data = {
            'name': 'Produto com Imagem',
            'category': 'Filtro',
            'value': 55.0,
            'description': 'Teste com imagem'
        }
        form = ProductForm(data=form_data, files={'img': image})
        self.assertTrue(form.is_valid())
