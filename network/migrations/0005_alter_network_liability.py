# Generated by Django 4.0 on 2024-07-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_alter_city_name_alter_country_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='network',
            name='liability',
            field=models.FloatField(default=0.0, verbose_name='Задолженность'),
        ),
    ]
