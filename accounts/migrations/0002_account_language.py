# Generated by Django 3.0.7 on 2020-08-14 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('pl', 'Polish'), ('da', 'Danish'), ('se', 'Swedish'), ('no', 'Norwegian')], default='en', max_length=10),
        ),
    ]
