# Generated by Django 3.1 on 2020-08-22 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200820_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='overview',
        ),
    ]