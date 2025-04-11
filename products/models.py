from django.db import models

categoryProduct = (
    ('1', 'Climatizador'),
    ('2', 'Cortina de Ar'),

)

mark = (
    ('1', 'LG'),
    ('2', 'Samsung')
)



class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    category = models.CharField(choices=categoryProduct)
    value = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=500)
    img = models.ImageField(null=True, blank=True, upload_to='products/')

    def __str__(self):
        return self.name
