# Generated by Django 3.0.7 on 2020-07-17 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_full_name', models.CharField(blank=True, max_length=70, null=True)),
                ('profile_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('profile_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('profile_address_line1', models.CharField(blank=True, max_length=80, null=True)),
                ('profile_address_line2', models.CharField(blank=True, max_length=80, null=True)),
                ('profile_town_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('profile_county', models.CharField(blank=True, max_length=80, null=True)),
                ('profile_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('profile_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
