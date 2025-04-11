from django.db import models


categoryService = (
    ('Conserto','Conserto'),
    ('Manutenção','Manutenção'),
    ('Instalação','Instalação'),
    ('Consulta', 'Consulta'),
    )

class Service(models.Model):
    id = models.BigAutoField(primary_key=True)
    service = models.CharField(max_length=50)
    category = models.CharField(choices=categoryService)
    value = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.service
