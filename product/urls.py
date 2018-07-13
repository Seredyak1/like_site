from django.urls import path
from product import views


urlpatterns = [
    path('<int:journey_id>/', views.journey_details, name='journey_details'),
    path('<int:journey_id>/comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:journey_id>/comment/create/', views.create_comment, name='create_comment'),
    path('<int:journey_id>/comment/<int:comment_id>/update', views.update_comment, name='update_comment')
 ]
