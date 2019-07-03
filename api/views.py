from rest_framework import generics, mixins, viewsets
from rest_framework import permissions

from .serializers import NewsSerializer, NewsPhotoSerializer
from news.models import News, NewsPhoto


#NEWS API VIEWS
class NewsAPIView(generics.ListAPIView):
    """
    list:
    Return a list of all news
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def get_queryset(self):
        queryset = News.objects.all().exclude(published=False)
        return queryset


class NewsDetailAPIView(generics.RetrieveAPIView):
    """
    get:
    Return one News obj by id
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    lookup_field = 'id'


class FirstNewsImageAPIView(generics.RetrieveAPIView):
    """
    get:
    Return first image of News
    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = NewsPhotoSerializer
    queryset = NewsPhoto.objects.all()
    lookup_field = "news_pk"


    def get_queryset(self):
        news = self.kwargs['news_pk']
        queryset = NewsPhoto.objects.filter(news=news).first()
        return queryset


