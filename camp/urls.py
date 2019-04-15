from django.urls import path
from camp import views

urlpatterns = [
    path('', views.get_camp_page, name='home_camp_page'),
    path('<str:slug>/', views.get_camp_detail, name='camp_detail'),
    path('<str:slug>/comment/<int:с_id>/delete/', views.camp_comment_delete, name='camp_comment_delete'),
    path('<str:slug>/comment/create/', views.camp_create_comment, name='camp_create_comment'),
    path('<str:slug>/comment/<int:с_id>/update', views.camp_update_comment, name='camp_update_comment')
]
