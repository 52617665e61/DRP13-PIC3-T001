from django import forms
from .models import Service
from django.contrib.admin.widgets import AdminDateWidget

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('service','category', 'value', 'description')

        labels = {
            'service': 'Serviço',
            'category': 'Categoria/Tipo de serviço',
            'value' :'valor',
            'description' :'Descrição do serviço prestado',
        }

