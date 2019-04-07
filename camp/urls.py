from django.urls import path
from camp import views

urlpatterns = [
    path('', views.get_camp_page, name='home_camp_page'),
]
