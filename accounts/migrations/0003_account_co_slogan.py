# Generated by Django 3.0.7 on 2020-08-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='co_slogan',
            field=models.CharField(default='No slogan', max_length=150),
        ),
    ]
