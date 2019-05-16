from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsListView.as_view(), name="news"),
    path('<int:news_id>/', views.NewsDetailViews.as_view(), name="news_detail"),
]
