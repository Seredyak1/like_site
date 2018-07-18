from django.shortcuts import render, get_object_or_404
from .utils import handle_pagination
from .models import News
from product.models import Category


def news(request):
    newses = News.objects.all().exclude(published=False)
    categories = Category.objects.all()
    return render(request, 'news/news.html', {'newses': handle_pagination(request, newses),
                                              'categories': categories})


def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    categories = Category.objects.all()
    return render(request, 'news/news_detail.html', {'news': news,
                                                     'categories': categories})
