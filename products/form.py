from django import forms
from .models import Product
from django.contrib.admin.widgets import AdminDateWidget

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','category', 'value', 'description', 'img')

        labels = {
            'service': 'Serviço',
            'category': 'Categoria/Tipo de serviço',
            'value' :'valor',
            'description' :'Descrição do serviço prestado',
            'imf' : 'Imagem do Producto'
        }

