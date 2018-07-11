from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .utils import handle_pagination

from .models import News


def news(request):
    newses = News.objects.all().exclude(published=False)
    return render(request, 'news/news.html', {'newses': handle_pagination(request, newses)})


def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(request, 'news/news_detail.html', {'news': news})
