from django import forms
from .models import Appoitment
from django.contrib.admin.widgets import AdminDateWidget


class AppoitmentForm(forms.ModelForm):
    class Meta:
        model = Appoitment
        fields = ('service', 'address', 'address_number', 'hour', 'description')

        labels = {
            'service': 'Serviço',
            'address': 'Endereço',
            'address_number' :'Número do endereço',
            'hour' :'Horário para visita',
            'description' : 'Descrição'
        }
