from django.urls import path

from .views import NewsAPIView, NewsDetailAPIView, FirstNewsImageAPIView

urlpatterns = [
    path('news/', NewsAPIView.as_view()),
    path('news/<int:id>/', NewsDetailAPIView.as_view()),
    path('news/<int:news_pk>/first_image/', FirstNewsImageAPIView.as_view())
]