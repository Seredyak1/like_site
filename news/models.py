from django.db import models


class News (models.Model):
    class Meta:
        ordering = ("-created_at",)

    title = models.CharField(max_length=255, blank=False)
    body = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
