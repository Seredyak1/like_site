from django.urls import path
from . import views


urlpatterns = [
    path('<int:journey_id>/', views.create_order, name="create_order"),
]
