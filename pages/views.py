from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render

from pages.forms import FeedbackForm
from pages.models import Feedback, Faq
from product.models import Category, Journey


def feedback(request):
    categories = Category.objects.all()
    """Create or show list for feedback"""
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш відгук буде опубліковано після перевірки модератором. Дякуємо!')

    form = FeedbackForm()

    feedbacks = Paginator(Feedback.objects.exclude(is_published=False), 10)
    page = request.GET.get('page')
    feedbacks = feedbacks.get_page(page)

    return render(request, 'pages/feedback.html', {'feedbacks': feedbacks, 'form': form, 'categories': categories})


def about_us(request):
    categories = Category.objects.all()
    return render(request, 'pages/about_us.html', {"categories": categories})


def get_faq(request):
    categories = Category.objects.all()
    faq = Faq.objects.all()
    return render(request, 'pages/faq.html', {'categories': categories, 'faq': faq})


def search(request):
    categories = Category.objects.all()
    query_journey_content = request.GET.get('q')
    query_category_id = request.GET.get('category_id')
    if query_category_id:
        journeys = Journey.objects.filter(category=query_category_id, description__icontains=query_journey_content)
        journeys_count = journeys.count()
        return render(request, 'pages/search.html', {'journeys': journeys, 'categories': categories,
                                                     ':query_journey_content':query_journey_content,
                                                     'query_category_id':query_category_id,
                                                     'journeys_count': journeys_count})
    else:
        journeys = Journey.objects.filter(description__icontains=query_journey_content)
        journeys_count = journeys.count()
        return render(request, 'pages/search.html', {'journeys': journeys, 'categories': categories,
                                                     ':query_journey_content':query_journey_content,
                                                     'journeys_count': journeys_count})

