from django.shortcuts import render, get_object_or_404
from django.views import generic, View

from .models import News
from product.models import Category


class NewsListView(generic.ListView):

    template_name = 'news/news.html'
    context_object_name = 'newses'
    paginate_by = 10

    def get_queryset(self):
        return News.objects.all().exclude(published=False)

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class NewsDetailViews(View):

    template_name = 'news/news_detail.html'

    def get(self, request, news_id, *args, **kwargs):
        news = get_object_or_404(News, id=news_id)
        categories = Category.objects.all()
        return render(request, 'news/news_detail.html', {'news': news,
                                                         'categories': categories})
