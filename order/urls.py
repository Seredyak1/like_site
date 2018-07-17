from django.urls import path
from . import views

urlpatterns = [
    path('order_for_anonim', views.order_anonim, name="order_anonim"),
]

