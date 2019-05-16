from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.FeedbackView.as_view(), name="feedback"),
    path('about_us/', views.about_us, name="about_us"),
    path('faq/', views.FAQView.as_view(), name="faq"),
    path('search/', views.search, name="search"),
    path('documents/', views.DocumentsView.as_view(), name="documents"),
    path('documents/download/<int:file_id>/', views.download_file, name="download_file"),
]
