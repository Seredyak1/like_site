from django.shortcuts import render
from product.models import Journey
from pages.models import Feedback
from news.models import News


def home(request):
    journeys = Journey.objects.all()[:8]
    feedbacks = Feedback.objects.all().exclude(is_published=False)[:5]
    newses = News.objects.last()
    return render(request, 'landing_page/home.html', {'journeys': journeys,
                                                      'feedbacks': feedbacks,
                                                      'newses': newses})
