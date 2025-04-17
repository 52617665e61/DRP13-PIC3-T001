from django import forms
from .models import Appoitment
from django.contrib.admin.widgets import AdminDateWidget


class AppoitmentForm(forms.ModelForm):
    class Meta:
        model = Appoitment
        fields = ('service', 'address', 'address_number', 'date','hour', 'description')

        labels = {
            'service': 'Serviço',
            'address': 'Endereço',
            'address_number' :'Número do endereço',
            'date' : 'Dia para visita',
            'hour' :'Horário para visita',
            'description' : 'Descrição'
        }

        widgets = {
            'date' : forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"})
        }


class UpdateAppoitmentForm(forms.ModelForm):
    class Meta:
        model = Appoitment
        fields = ('status',)

        labels = {
            'status' : 'Estado'
        }
