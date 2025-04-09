from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    primeiroNome = models.CharField(max_length=14, null=True)
    ultimoNome=models.CharField(max_length=14, null=True)
    


