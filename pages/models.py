from django.db import models


class Client_Company(models.Model):
    title = models.CharField(max_length=255, verbose_name='company_title', blank=True)
    logo = models.ImageField(upload_to='companies-logo')
    site = models.CharField(max_length=255, verbose_name='site_address', blank=True)


class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name='name', blank=True)
    body_text = models.TextField(verbose_name='description')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
