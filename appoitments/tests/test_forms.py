from django.test import TestCase
from appoitments.forms import AppoitmentForm
from services.models import Service  # Certifique-se de importar do app correto
import datetime

class AppoitmentFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.service = Service.objects.create(
            service="Serviço Teste",
            category="Instalação",  # Um dos valores válidos
            value="150.00",
            description="Descrição teste"
        )

    def test_form_valid_data(self):
        form_data = {
            'service': self.service.id,  # usa o ID do objeto real
            'address': 'Rua Teste',
            'address_number': 123,
            'date': '2025-05-23',
            'hour': '08:00',
            'description': 'Teste descrição'
        }

        form = AppoitmentForm(data=form_data)
        # adiciona choices válidas para o campo hour
        form.fields['hour'].choices = [(f"{h:02d}:00", f"{h:02d}:00") for h in range(8, 19)]

        print("Form errors:", form.errors)
        self.assertTrue(form.is_valid())