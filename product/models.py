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
        verbose_name = "Пригода"
        verbose_name_plural = "Пригоди"
        ordering = ('-updated_at',)

    sku = models.CharField(max_length=255, verbose_name='Номер')
    title = models.CharField(max_length=255, verbose_name='Назва пригоди')
    description = models.TextField(verbose_name='Опис пригоди')
    durations_days = models.IntegerField(verbose_name='Тривалість днів')
    durations_night = models.IntegerField(verbose_name='Тривалість ночей')
    price = models.IntegerField(verbose_name='Ціна')
    sale_price = models.IntegerField(verbose_name='Ціна зі скидкою', null=True, blank=True)
    category = models.ForeignKey(Category, related_name='Journeys', on_delete=models.CASCADE, verbose_name='Категорія')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата останнього оновлення')

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
