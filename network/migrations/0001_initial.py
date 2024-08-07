# Generated by Django 4.0 on 2024-07-22 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('liability', models.FloatField(verbose_name='Задолженность')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_networks', to='network.network', verbose_name='Поставщик')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('model', models.CharField(max_length=200, verbose_name='Модель')),
                ('launch_date', models.DateTimeField(verbose_name='Дата запуска продукта')),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='network.network', verbose_name='Поставщик')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='Номер дома')),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='network.network', verbose_name='Поставщик')),
            ],
        ),
    ]
