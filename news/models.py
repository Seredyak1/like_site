from django.db import models
from ckeditor.fields import RichTextField
from django.db.models import F
from django.utils.translation import gettext_lazy as _, get_language


class NewsManager(models.Manager):

    def get_queryset(self):
        locale = get_language()
        return super().get_queryset().annotate(title=F('title_' + locale), body=F('body_' + locale),
                                               short_description=F('short_description_' + locale),
                                               seo_title=F('seo_title_' + locale))


class News (models.Model):
    class Meta:
        verbose_name = _('Новини')
        ordering = ("-created_at",)

    title_uk = models.CharField(max_length=255, blank=False)
    title_en = models.CharField(max_length=255, blank=True)
    seo_title_uk = models.CharField(max_length=255, blank=True)
    seo_title_en = models.CharField(max_length=255, blank=True)
    short_description_uk = RichTextField(blank=False)
    short_description_en = RichTextField(blank=True)
    body_uk = RichTextField(blank=False)
    body_en = RichTextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    objects = NewsManager()

    def __str__(self):
        return self.title_uk

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('news_detail', args=[str(self.id)])


class NewsPhoto(models.Model):
    news = models.ForeignKey(News, related_name='news_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news-photos')
