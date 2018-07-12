from django.urls import path
from product import views
from product.models import Category


urlpatterns = [
    path('<str:slug>', views.category_detail, name='category_detail'),
]
