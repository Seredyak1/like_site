from django.contrib.auth.models import User
from django.db import models

from product.models import Journey


class Order(models.Model):
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    ORDER_STATUS_CHOICES = (
        (0, 'New'),
        (1, 'Paid'),
        (2, 'Send to Client'),
    )

    user = models.ForeignKey(User, verbose_name='Buyer', on_delete=False)
    journey = models.ForeignKey(Journey, related_name='in_orders', on_delete=False)
    track_number = models.CharField(max_length=255, verbose_name='Track Number', blank=True)
    email_address = models.CharField(max_length=255, verbose_name='Email Address', blank=False)
    contact_phone = models.CharField(max_length=255, verbose_name='Contact phone', blank=False)
    status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_CHOICES[0][0])
    total = models.IntegerField(verbose_name='Total price', null=True)
    persons = models.IntegerField(verbose_name='Persons', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    contacted = models.BooleanField(verbose_name="Зконтактовано")

    def __str__(self):
        return "Order # " + str(self.pk)


class OrderAnonim(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    person = models.IntegerField(blank=True)
    duration = models.IntegerField(blank=False)
    email = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=False)
    contacted = models.BooleanField(verbose_name="Зконтактовано", default=False)

    def __str__(self):
        return "Order # " + str(self.name)