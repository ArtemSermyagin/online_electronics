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

    class Meta:
        verbose_name = 'Сеть'
        verbose_name_plural = 'Сети'

    def __str__(self):
        return f"{self.name} {self.liability}"


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities', verbose_name='Страна')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f"{self.name} {self.country}"


class Contact(models.Model):
    email = models.EmailField(verbose_name='Почта')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    network = models.ForeignKey(Network, on_delete=models.CASCADE, related_name='contacts', verbose_name='Поставщик')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='contacts', verbose_name='Город')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f"{self.email} {self.city} {self.street} {self.network.id}"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=200, verbose_name='Модель')
    launch_date = models.DateTimeField(verbose_name='Дата запуска продукта')
    network = models.ForeignKey(Network, on_delete=models.CASCADE, related_name='products', verbose_name='Поставщик')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f"{self.name} {self.model} {self.network.id}"
