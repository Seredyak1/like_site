from django.db import models


class ClientCompany(models.Model):
    class Meta:
        verbose_name = "Клієнт-Компанія"
        verbose_name_plural = "Клієнт-Компанії"

    title = models.CharField(max_length=255, verbose_name='Назва компанії', blank=True)
    logo = models.ImageField(upload_to='companies-logo', verbose_name='Лого')
    site = models.CharField(max_length=255, verbose_name='Сайт', blank=True)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"

    name = models.CharField(max_length=255, verbose_name='Імя', blank=True)
    body_text = models.TextField(verbose_name='Відгук')
    created_at = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубліковано?')

    def __str__(self):
        return self.name
