# Generated by Django 3.2.3 on 2021-05-28 18:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Forecast', '0003_alter_buy_buy_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='buy_datetime',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
