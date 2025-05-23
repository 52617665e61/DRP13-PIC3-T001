# Generated by Django 5.2 on 2025-04-08 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('1', 'Climatizador'), ('2', 'Cortina de Ar')])),
                ('value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('description', models.CharField(max_length=500)),
                ('img', models.ImageField(blank=True, null=True, upload_to='products/')),
            ],
        ),
    ]
