from django.urls import path
from rest_framework import routers

from .views import *

urlpatterns = [
    path('news/', NewsAPIView.as_view()),
    path('news/<int:id>/', NewsDetailAPIView.as_view()),

    path('companies/', ClientCompanyAPIViews.as_view()),
    path('documents/', DocumentsApiView.as_view()),
    path('faq/', FaqAPIView.as_view()),
    path('feedback/', FeedbackAPIView.as_view()),

    path('camps/', CampsAPIView.as_view()),
    path('camps/<str:slug>/', CampDetailAPIView.as_view()),
    path('camps/<str:slug>/comments/', CampCommentsAPIView.as_view()),
    path('camps/<str:slug>/comments/<int:id>/', CampCommentUpdateOrDeleteApiView.as_view()),

    path('categories/', CategoryListAPIView.as_view()),
    path('category/<str:slug>/', CategoryDetailAPIView.as_view()),
    path('journey_card/', JourneyCardListAPIView.as_view()),
    path('journey_card/<str:slug>/', JourneyCardListWithCategoryAPIView.as_view()),
    path('journey_card_new/', JourneyCardListForNewAPIView.as_view()),
    path('journey_card_with_sale/', JourneyCardListWithSalePriceAPIView.as_view()),
    path('journey/<int:id>/', JourneyDetailAPIView.as_view()),
    path('journey/<int:journey_id>/comments/', JourneyCommentsAPIView.as_view()),
    path('journey/<int:journey_id>/comments/<int:id>/', JourneyCommentsUpdateAndDeleteAPIView.as_view()),

    path('order_anonim/', OrderAnonimAPIView.as_view()),
    path('order/<int:journey_id>/', OrderAPIView.as_view()),

]
