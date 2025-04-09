from django.db import models
from  services.models import Service



class Appoitment(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.IntegerField()
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=50)
    address_number = models.IntegerField()
    hour = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
