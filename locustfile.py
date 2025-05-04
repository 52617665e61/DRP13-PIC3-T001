from locust import HttpUser, task, between
from locust.clients import ResponseError
import random
import re

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # tempo entre tarefas (simula usuários reais)

    def on_start(self):
        """Executado antes de qualquer tarefa ser feita. Aqui, logamos o usuário para poder acessar as views protegidas."""
        self.login()

    def login(self):
        """Método para fazer login na aplicação e salvar o cookie de sessão com o CSRF token."""
        # Faz a requisição GET na página de login para obter o token CSRF
        response = self.client.get("/login/")
        
        # Verifica se o CSRF token foi encontrado na página
        csrf_token = self.extract_csrf_token(response.text)
        if not csrf_token:
            raise ResponseError("CSRF token não encontrado!")

        # Agora realiza o POST de login com o token CSRF
        response = self.client.post("/login/", {
            "username": "testuser",  # Substitua por um usuário real de teste
            "password": "testpassword",  # Substitua pela senha do usuário
            "csrfmiddlewaretoken": csrf_token,  # Inclui o token CSRF
        })

        if response.status_code != 200:
            raise ResponseError(f"Falha no login: {response.status_code}")

    def extract_csrf_token(self, page_html):
        """Extrai o token CSRF do HTML da página."""
        # Regex para pegar o valor do CSRF token
        match = re.search(r'csrfmiddlewaretoken" value="([^"]+)"', page_html)
        if match:
            return match.group(1)
        return None

    @task(2)
    def list_appointments(self):
        """Testa a lista de agendamentos."""
        self.client.get("/appoitmentsList")

    @task(3)
    def get_available_hours(self):
        """Testa a consulta de horários disponíveis via Ajax."""
        date = "2025-05-03"
        self.client.get(f"/get-available-hours/?date={date}")

    @task(1)
    def appointment_info(self):
        """Testa a página de informações do agendamento."""
        self.client.get("/appoitmentList/1")

    @task(1)
    def post_appointment(self):
        """Testa o envio de um novo agendamento."""
        # Gerando dados para o formulário
        hour = random.choice([f"{h:02d}:00" for h in range(8, 19)])  # Escolhendo uma hora aleatória
        data = {
            "service": "Limpeza",  # Substitua por um serviço real
            "address": "Rua Teste, 123",  # Substitua por um endereço real
            "address_number": "123",  # Número do endereço
            "date": "2025-05-03",  # Data do agendamento
            "hour": hour,  # Hora aleatória escolhida
            "description": "Agendamento de teste",  # Descrição do agendamento
        }

        # Faz a requisição GET para pegar o CSRF token
        response = self.client.get("/addAppoitment")
        csrf_token = self.extract_csrf_token(response.text)
        if not csrf_token:
            raise ResponseError("CSRF token não encontrado!")

        # Faz a requisição POST para criar o agendamento com os dados do formulário
        response = self.client.post("/addAppoitment", {
            "service": data["service"],
            "address": data["address"],
            "address_number": data["address_number"],
            "date": data["date"],
            "hour": data["hour"],
            "description": data["description"],
            "csrfmiddlewaretoken": csrf_token,  # Inclui o token CSRF
        })

        if response.status_code != 200:
            raise ResponseError(f"Falha ao agendar: {response.status_code}")

