from django.urls import path
from . import views

urlpatterns = [
    path('feedback', views.feedback, name="feedback"),
    path('about_us', views.about_us, name="about_us"),
    path('faq', views.get_faq, name="faq"),
    path('search', views.search, name="search"),
    path('documents', views.documents, name="documents"),
    path('documents/download/<int:file_id>', views.download_file, name="download_file"),
]
