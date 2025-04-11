from django.db import models


categoryService = (
    ('1','Conserto'),
    ('2','Manutenção'),
    ('3','Instalação')
    )

class Service(models.Model):
    id = models.BigAutoField(primary_key=True)
    service = models.CharField(max_length=30)
    category = models.CharField(choices=categoryService)
    value = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.service
