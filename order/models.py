from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from product.models import Journey


class Order(models.Model):
    class Meta:
        verbose_name = _("Замовлення")
        verbose_name_plural = _("Замовлення")

    ORDER_STATUS_CHOICES = (
        (0, _('Нове')),
        (1, _('Оплачене')),
    )

    user = models.ForeignKey(User, verbose_name=_('Покупець'), on_delete=False)
    journey = models.ForeignKey(Journey, related_name='in_orders', on_delete=False)
    email_address = models.CharField(max_length=255, verbose_name='Email адрес', blank=False)
    contact_phone = models.CharField(max_length=255, verbose_name=_('Номер телефону'), blank=False)
    status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_CHOICES[0][0])
    total = models.IntegerField(verbose_name=_('Загальна ціна'), null=True)
    persons = models.IntegerField(verbose_name='Кількість людей', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    contacted = models.BooleanField(verbose_name="Зконтактовано", default=False)

    def __str__(self):
        return _("Order # ") + str(self.pk)


class OrderAnonim(models.Model):
    class Meta:
        verbose_name = _("Анонімне замовлення")
        verbose_name_plural = _("Анонімні замовлення")

    name = models.CharField(max_length=255, blank=False, verbose_name=_('ПІБ'))
    description = models.TextField(blank=False, verbose_name=_('Опис'))
    person = models.IntegerField(blank=True, verbose_name=_('Кількість осіб'))
    duration = models.IntegerField(blank=False, verbose_name=_('Тривалість'))
    email = models.CharField(max_length=255, blank=True, verbose_name=_('Email'))
    phone = models.CharField(max_length=255, blank=False, verbose_name=_('Телефон'))
    contacted = models.BooleanField(verbose_name="Зконтактовано", default=False)

    def __str__(self):
        return _("Order # ") + str(self.name)
