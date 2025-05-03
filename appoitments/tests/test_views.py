from django.test import TestCase
from django.urls import reverse
from appoitments.models import Appoitment
from services.models import Service  # Corrija se o nome do app for diferente
from datetime import date, time
from django.contrib.auth import get_user_model

User = get_user_model()

class AppoitmentViewTest(TestCase):
    def setUp(self):
        # Criação do usuário
        self.user = User.objects.create_user(
            email='teste@test.com',
            user_name='testuser',
            password='password',
            password2='password',
            first_name='Test',
            last_name='User',
        )
        
        # Login do usuário
        self.client.login(user_name='testuser', password='password')
        
        # Criação do serviço
        self.service = Service.objects.create(
            service="Teste",
            category="Consulta",
            value="50",
            description="Descrição teste"
        )
        
        # Criação do agendamento
        self.appoitment = Appoitment.objects.create(
            user=self.user.user_name,
            name=f"{self.user.first_name} {self.user.last_name}",
            service=self.service,
            address="Rua A",
            address_number=123,
            date=date.today(),
            hour=time(10, 0),
            description="Agendamento de teste"
        )

    def test_view_status_code(self):
        response = self.client.get(reverse('addAppoitment'))
        self.assertEqual(response.status_code, 200)

    def test_view_template_used(self):
        response = self.client.get(reverse('addAppoitment'))
        self.assertTemplateUsed(response, 'appoitments/appoitmentRegister.html')

    def test_view_context_data(self):
        response = self.client.get(reverse('addAppoitment'))
        self.assertIn('form', response.context)