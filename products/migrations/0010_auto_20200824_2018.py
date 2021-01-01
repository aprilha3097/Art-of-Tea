# Generated by Django 3.0.7 on 2020-08-24 19:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_discontinued'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='duration',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(24)]),
        ),
    ]