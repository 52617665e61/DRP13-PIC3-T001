# Generated by Django 5.2 on 2025-04-11 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoitments', '0002_alter_appoitment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoitment',
            name='date',
            field=models.CharField(max_length=8),
        ),
    ]
