# Generated by Django 5.2 on 2025-04-11 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoitments', '0008_alter_appoitment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoitment',
            name='status',
            field=models.CharField(choices=[('1', 'Visita em aberto'), ('2', 'A caminho'), ('3', 'Situação pendente'), ('4', 'Concluido')], default='Visita em aberto', max_length=20),
        ),
    ]
