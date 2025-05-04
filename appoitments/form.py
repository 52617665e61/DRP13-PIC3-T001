from django import forms
from .models import Appoitment
from django.contrib.admin.widgets import AdminDateWidget
import datetime


class AppoitmentForm(forms.ModelForm):

    hour = forms.ChoiceField(choices=[], label="Horário para visita")

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
            'date' : forms.DateInput(format="%Y-%m-%d", attrs={"type": "date", "id": "id_date"})
        }
        
    def __init__(self, *args, **kwargs):
        super(AppoitmentForm, self).__init__(*args, **kwargs)

        data = kwargs.get('data')
        if data:
            date = data.get('date')
            if date:
                self.fields['hour'].choices = self.get_available_hours_for_date(date)   
        else:
            # Preenche com todos os horários se nenhum for informado
            self.fields['hour'].choices = [(f"{h:02d}:00", f"{h:02d}:00") for h in range(8, 19)]

    def get_available_hours_for_date(self, date):
        taken = Appoitment.objects.filter(date=date).values_list('hour', flat=True)
        all_hours = [f"{h:02d}:00" for h in range(8, 19)]
        taken_hours = [t.strftime('%H:%M') for t in taken]
        available = [(h, h) for h in all_hours if h not in taken_hours]
        return available


class UpdateAppoitmentForm(forms.ModelForm):
    class Meta:
        model = Appoitment
        fields = ('status',)

        labels = {
            'status' : 'Estado'
        }
