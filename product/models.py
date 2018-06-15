from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    name= models.CharField(max_length=255, verbose_name=('Name of Category'))
    description_en = models.TextField(verbose_name=('Description of Category'))


class Jorney(models.Model):
    class Meta:
        verbose_name = ("Jorney")
        verbose_name_plural = ("Jorneys")
        ordering = ['-updated_at']

    sku = models.CharField(max_length=255, verbose_name=('SKU'))
    title_en = models.CharField(max_length=255, verbose_name=('Name of Jorney'))
    description_en = models.TextField(verbose_name=('Description of Jorney'))
    durations_days = models.IntegerField(verbose_name=('Durations in days'))
    durations_night = models.IntegerField(verbose_name=('Durations in days'))
    price = models.IntegerField(verbose_name=('Price'))
    sale_price = models.IntegerField(verbose_name=('Sale Price'), null=True, blank=True)
    category = models.ForeignKey(Category, related_name='jorneys', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if not hasattr(self, 'title'):
            return self.title_en
        return self.title

class JorneyPhoto(models.Model):
    jorney = models.ForeignKey(Jorney, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item-photos')


class Comment(models.Model):
    jorney = models.ForeignKey(Jorney, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=False)
    body = models.TextField(verbose_name=('Comment text'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
