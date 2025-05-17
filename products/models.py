from django.db import models
from django.core.validators import MinValueValidator

categoryProduct = (
    ('Climatizador', 'Climatizador'),
    ('Cortina de Ar', 'Cortina de Ar'),
    ('Ar condicionado', 'Ar condicionado'),
    ('Filtro', 'Filtro'),
    ('Cabo', 'Cabo'),

)

mark = (
    ('Marca1', 'Marca1'),
    ('Marca2', 'Marca2'),
    ('Marca3', 'Marca3'),
)


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(choices=categoryProduct)
    value = models.DecimalField(max_digits=100, decimal_places=2, validators=[MinValueValidator(0.01)])
    description = models.CharField(max_length=500)
    img = models.ImageField(null=True, blank=True, upload_to='products/')

    def __str__(self):
        return self.name
