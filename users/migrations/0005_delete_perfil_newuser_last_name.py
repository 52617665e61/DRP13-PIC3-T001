# Generated by Django 5.2 on 2025-04-10 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_newuser_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Perfil',
        ),
        migrations.AddField(
            model_name='newuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
