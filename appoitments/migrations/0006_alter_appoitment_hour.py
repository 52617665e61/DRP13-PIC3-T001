# Generated by Django 5.2 on 2025-04-17 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoitments', '0005_alter_appoitment_date_alter_appoitment_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoitment',
            name='hour',
            field=models.CharField(),
        ),
    ]
