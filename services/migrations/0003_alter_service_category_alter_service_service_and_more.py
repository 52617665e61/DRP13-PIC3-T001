# Generated by Django 5.2 on 2025-04-11 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_service_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.CharField(choices=[('Conserto', 'Conserto'), ('Manutenção', 'Manutenção'), ('Instalação', 'Instalação')]),
        ),
        migrations.AlterField(
            model_name='service',
            name='service',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='service',
            name='value',
            field=models.CharField(max_length=100),
        ),
    ]
