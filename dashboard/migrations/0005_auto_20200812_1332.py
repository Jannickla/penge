# Generated by Django 3.0.7 on 2020-08-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_delete_invoicequantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date'),
        ),
    ]
