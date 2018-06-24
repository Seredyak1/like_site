from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    name = models.CharField(max_length=255, verbose_name='Назва Категорії')
    slug = models.SlugField(unique=True, default='', verbose_name='Назва в URL')
    description = models.TextField(verbose_name='Опис Категорії')
    category_logo = models.ImageField(upload_to='category-logo', null=True, verbose_name='Катринка Категорії')

    def __str__(self):
        return self.name


class Journey(models.Model):
    class Meta:
        verbose_name = "Journey"
        verbose_name_plural = "Journeys"
        ordering = ['-updated_at']

    sku = models.CharField(max_length=255, verbose_name='SKU')
    title = models.CharField(max_length=255, verbose_name='Name of Journey')
    description = models.TextField(verbose_name='Description of Journey')
    durations_days = models.IntegerField(verbose_name='Durations in days')
    durations_night = models.IntegerField(verbose_name='Durations in night')
    price = models.IntegerField(verbose_name='Price')
    sale_price = models.IntegerField(verbose_name='Sale Price', null=True, blank=True)
    category = models.ForeignKey(Category, related_name='Journeys', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class JourneyPhoto(models.Model):
    journey = models.ForeignKey(Journey, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='journeys-photos')


class Comment(models.Model):
    class Meta:
        ordering = ('-created_at',)

    journey = models.ForeignKey(Journey, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=False)
    body = models.TextField(verbose_name='Comment text')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
