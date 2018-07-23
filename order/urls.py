from django.urls import path
from . import views


urlpatterns = [
    path('<int:journey_id>/', views.create_order, name="create_order"),
    path('<int:journey_id>/', views.add_person, name="add_person"),
    path('order_for_anonim', views.order_anonim, name="order_anonim"),
]
