from django.contrib.auth.models import User
from django.db import models
from product.models import Journey


class Order(models.Model):
    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    ORDER_STATUS_CHOICES = (
        (0, 'Нове'),
        (1, 'Оплачене'),
    )

    user = models.ForeignKey(User, verbose_name='Покупець', on_delete=False)
    journey = models.ForeignKey(Journey, related_name='in_orders', on_delete=False)
    email_address = models.CharField(max_length=255, verbose_name='Email адрес', blank=False)
    contact_phone = models.CharField(max_length=255, verbose_name='Номер телефону', blank=False)
    status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_CHOICES[0][0])
    total = models.IntegerField(verbose_name='Загальна ціна', null=True)
    persons = models.IntegerField(verbose_name='Люди', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    contacted = models.BooleanField(verbose_name="Зконтактовано", default=False)

    def __str__(self):
        return "Order # " + str(self.pk)


class OrderAnonim(models.Model):
    class Meta:
        verbose_name = "Анонімне замовлення"
        verbose_name_plural = "Анонімні замовлення"

    name = models.CharField(max_length=255, blank=False, verbose_name='ПІБ')
    description = models.TextField(blank=False, verbose_name='Опис')
    person = models.IntegerField(blank=True, verbose_name='Кількість осіб')
    duration = models.IntegerField(blank=False, verbose_name='Тривалість')
    email = models.CharField(max_length=255, blank=True, verbose_name='Email')
    phone = models.CharField(max_length=255, blank=False, verbose_name='Телефон')
    contacted = models.BooleanField(verbose_name="Зконтактовано", default=False)

    def __str__(self):
        return "Order # " + str(self.name)