from django.db import models
from  services.models import Service
from users.models import NewUser
import datetime

status = (
    ('Visita em aberto', 'Visita em aberto'),
    ('A caminho', 'A caminho'),
    ('Situação pendente', 'Situação pendente'),
    ('Concluido', 'Concluido')
)

class Appoitment(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.CharField()
    name = models.CharField()
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=50)
    address_number = models.IntegerField()
    date = models.DateField()
    hour = models.TimeField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=status, default='Visita em aberto')
