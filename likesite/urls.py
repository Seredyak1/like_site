"""likesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from likesite.sitemap import StaticViewSitemap, CategorySitemap, JourneySitemap, NewsViewSitemap
from product import views as views_product
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

sitemaps = {
    'journey': JourneySitemap,
    'static': StaticViewSitemap,
    'category': CategorySitemap,
    'news': NewsViewSitemap,
}

urlpatterns = []

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('landing_page.urls')),
    path('category/', include('product.category_urls')),
    path('home/', include('pages.urls')),
    path('accounts/', include('allauth.urls')),
    path('news/', include('news.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('order/', include('order.urls')),
    path('journey/', include('product.urls')),
    path('new/', views_product.get_category_new, name="new"),
    path('hot_sale/', views_product.get_category_sale, name="hot_sales"),
    path('i18n/', include('django.conf.urls.i18n')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('camps/', include('camp.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
)

urlpatterns += [
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('swagger/', schema_view),
]

urlpatterns += [
    url(r'^__debug__/', include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
