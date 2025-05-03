from django.test import TestCase
from appoitments.models import Appoitment
from services.models import Service  # ajuste conforme a localização real do modelo Service

class AppoitmentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.service = Service.objects.create(service="Serviço Teste")
        cls.appoitment = Appoitment.objects.create(
            service=cls.service,
            address='Rua Teste',
            address_number=123,
            date='2025-05-23',
            hour='10:00',
            description='Descrição Teste',
            status='Visita em aberto'
        )

    def test_model_fields(self):
        appoitment = self.appoitment
        self.assertEqual(appoitment.service.service, 'Serviço Teste')
        self.assertEqual(appoitment.address, 'Rua Teste')
        self.assertEqual(appoitment.address_number, 123)
        self.assertEqual(str(appoitment.date), '2025-05-23')
        self.assertEqual(str(appoitment.hour), '10:00')
        self.assertEqual(appoitment.description, 'Descrição Teste')
        self.assertEqual(appoitment.status, 'Visita em aberto')

