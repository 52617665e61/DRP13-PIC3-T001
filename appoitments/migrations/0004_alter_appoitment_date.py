# Generated by Django 5.2 on 2025-04-17 19:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoitments', '0003_alter_appoitment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoitment',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.date),
        ),
    ]
