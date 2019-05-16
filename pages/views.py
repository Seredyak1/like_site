import os
import mimetypes
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse
from django.views import generic, View

from pages.forms import FeedbackForm
from pages.models import Feedback, Faq, Document
from product.models import Category, Journey


class FeedbackView(View):

    template_name = 'pages/feedback.html'
    form_class = FeedbackForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        feedbacks = Feedback.objects.all().exclude(is_published=False)
        return render(request, self.template_name, {'form': form,
                                                    'feedbacks': feedbacks})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Ваш відгук буде опубліковано після перевірки модератором. Дякуємо!'))
            return redirect('feedback')

        return render(request, self.template_name, {'form': form})


def about_us(request):
    categories = Category.objects.all()
    massive_text = _("""
    - унікальний куточок України. Водночас тут можна побачити
        холодні вершини Карпат та відчути тепло Закарпатської долини, здійснити подорож гірською полониною та відпочити
        у гарячих термальних басейнах. Це мультикультурний край, що представлений сотнею різних національностей та етносів, та у якому
        можна побачити архітектурні стилі з усієї Європи та світу. До сьогодні тут збережений унікальний діалект української мови
        складений зі слів кожного народу, хто колись проживав чи проживає на Закарпатті, та що змінюється від села до села,
        від регіону до регіону. Тільки тут можна скуштувати безліч різномінітних страв української, угорської, румунської, чеської,
        німецької та інших кухонь, спробувати світових сортів вина. Саме такою є земля, наближена до небa!""")
    return render(request, 'pages/about_us.html', {"categories": categories, "massive_text": massive_text})


class FAQView(generic.ListView):

    template_name = 'pages/faq.html'
    model = Faq
    context_object_name = 'faq'

    def get_context_data(self, **kwargs):
        context = super(FAQView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


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


class DocumentsView(generic.ListView):

    template_name = 'pages/documents.html'
    model = Document
    context_object_name = 'documents'

    def get_context_data(self, **kwargs):
        context = super(DocumentsView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


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
