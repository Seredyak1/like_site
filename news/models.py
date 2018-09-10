from django.db import models
from ckeditor.fields import RichTextField


class News (models.Model):
    class Meta:
        ordering = ("-created_at",)

    title = models.CharField(max_length=255, blank=False)
    seo_title = models.CharField(max_length=255, blank=True)
    short_description = RichTextField(blank=False)
    body = RichTextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('news_detail', args=[str(self.id)])


class NewsPhoto(models.Model):
    news = models.ForeignKey(News, related_name='news_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news-photos')
