from django.urls import path
from . import views


urlpatterns = [
    path('journey/<int:journey_id>/', views.create_order, name="create_order"),
    path('journey/<int:journey_id>/update_persons/', views.update_persons, name="update_persons"),
    path('order_for_anonim', views.order_anonim, name="order_anonim"),
]
