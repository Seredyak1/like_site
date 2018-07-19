from django.urls import path
from . import views


urlpatterns = [
    path('<int:journey_id>/order', views.create_order, name="create_order"),
    path('order_for_anonim', views.order_anonim, name="order_anonim"),
]
