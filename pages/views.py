from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from pages.forms import FeedbackForm
from pages.models import Feedback, Faq, Document
from product.models import Category, Journey
import os
import mimetypes
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse


def feedback(request):
    categories = Category.objects.all()
    """Create or show list for feedback"""
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Ваш відгук буде опубліковано після перевірки модератором. Дякуємо!'))

    form = FeedbackForm()

    feedbacks = Paginator(Feedback.objects.exclude(is_published=False), 10)
    page = request.GET.get('page')
    feedbacks = feedbacks.get_page(page)

    return render(request, 'pages/feedback.html', {'feedbacks': feedbacks, 'form': form, 'categories': categories})


def about_us(request):
    categories = Category.objects.all()
    massive_text = _("""
    - унікальний куточок України. Водночас тут можна побачити
        холодні вершини Карпат та відчути тепло Закарпатської долини, здійснити подорож гірською полониною та відпочити
        у гарячих термальних басейнах. Це мультикультурний край, що представлений сотнею різних національностей та етносів,
        побачити архітектурні стилі з усієї Європи та світу. До сьогодні тут збережений унікальний діалект української мови
        складений зі слів кожного народу, хто колись проживав чи проживає на Закарпатті, та що змінюється від села до села,
        від регіону до регіону. Тільки тут можна скуштувати безліч різномінітних страв української, угорської, румунської, чеської,
        німецькою та десятків ніших кухонь, спробувати світових сортів вина. Саме такою є земля, наближена до небa!""")
    return render(request, 'pages/about_us.html', {"categories": categories, "massive_text": massive_text})


def get_faq(request):
    categories = Category.objects.all()
    faq = Faq.objects.all()
    return render(request, 'pages/faq.html', {'categories': categories, 'faq': faq})


def search(request):
    categories = Category.objects.all()
    query_search = request.GET.get('q')
    query_category_id = request.GET.get('category_id')
    if query_category_id:
        journeys = Journey.objects.filter(category=query_category_id).filter(Q(description__icontains=query_search) | Q(title__icontains=query_search))
        journeys_count = journeys.count()
        return render(request, 'pages/search.html', {'journeys': journeys, 'categories': categories,
                                                     'query_search':query_search,
                                                     'query_category_id':query_category_id,
                                                     'journeys_count': journeys_count})
    else:
        journeys = Journey.objects.filter(Q(description__icontains=query_search) | Q(title__icontains=query_search))
        journeys_count = journeys.count()
        return render(request, 'pages/search.html', {'journeys': journeys, 'categories': categories,
                                                     'query_search': query_search,
                                                     'journeys_count': journeys_count})


def documents(request):
    documents = Document.objects.all()
    categories = Category.objects.all()

    return render(request, 'pages/documents.html', {'documents': documents, 'categories': categories})


def download_file(request, file_id):
        document_for_download = Document.objects.get(id=file_id)
        path = document_for_download.document.path
        content_type = mimetypes.guess_type(path)
        if os.path.exists(path):
            with open(path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type=content_type[0])
                f_extension = str(document_for_download.document).rpartition('.')[-1]
                response['Content-Disposition'] = 'attachment; filename={}.{}'.format(document_for_download.title_doc,
                                                                                  f_extension)
                return response
