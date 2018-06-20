from django.contrib import admin
from .models import News, NewsPhoto


class NewsPhotoInline(admin.TabularInline):
    model = NewsPhoto
    extra = 0


class NewsAdmin(admin.ModelAdmin):
    """Add photos to Item in Admin"""
    inlines = [NewsPhotoInline]


admin.site.register(News, NewsAdmin)
