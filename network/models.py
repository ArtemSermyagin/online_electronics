from django.db import models


class Network(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    network = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='child_networks',
        null=True,
        blank=True,
        verbose_name='Поставщик'
    )
    liability = models.FloatField(verbose_name='Задолженность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.name} {self.liability} {self.created_at}"


class Contact(models.Model):
    email = models.EmailField(verbose_name='Почта')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    network = models.ForeignKey(Network, on_delete=models.CASCADE, related_name='contacts', verbose_name='Поставщик')

    def __str__(self):
        return f"{self.country} {self.city} {self.street} {self.network.id}"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=200, verbose_name='Модель')
    launch_date = models.DateTimeField(verbose_name='Дата запуска продукта')
    network = models.ForeignKey(Network, on_delete=models.CASCADE, related_name='products', verbose_name='Поставщик')

    def __str__(self):
        return f"{self.name} {self.model} {self.network.id}"
