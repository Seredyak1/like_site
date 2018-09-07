from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from product.models import Journey, Category


class JourneySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Journey.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Category.objects.all()


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'about_us', 'faq', 'documents', 'feedback']

    def location(self, item):
        return reverse(item)