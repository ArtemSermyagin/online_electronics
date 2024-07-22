from django.db import models


class Network(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    country = models.CharField(max_length=50, verbose_name='Страна')
    provider = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child_networks')
    liability = models.FloatField(verbose_name='Задолженность')
    time_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.name} {self.provider} {self.liability} {self.time_creation}"


class Contacts(models.Model):
    email = models.EmailField()
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Город')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    network = models.ForeignKey(Network, on_delete=models.CASCADE, verbose_name='Сеть')

    def __str__(self):
        return f"{self.network} {self.country} {self.email}"

class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=200, verbose_name='Модель')
    product_launch_date = models.DateTimeField(verbose_name='Дата запуска продукта')
    provider = models.ForeignKey(Network, on_delete=models.CASCADE, related_name='child_networks')

    def __str__(self):
        return f"{self.name} {self.provider} {self.model}"

