# Generated by Django 3.1 on 2020-09-01 16:00

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_auto_20200831_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='co_country',
            field=django_countries.fields.CountryField(max_length=50),
        ),
    ]
