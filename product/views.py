from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .forms import CommentForm, Comment
from product.models import Category, Journey
from product.utils import handle_pagination


def journey_details(request, journey_id):
    journey = Journey.objects.filter(id=journey_id).first()
    if not journey:
        raise Http404

    categories = Category.objects.all()
    comments = Comment.objects.filter(journey=journey).exclude(is_published=False)
    form = CommentForm()
    return render(request, 'product/journey_detail.html', {'journey': journey,
                                                           'categories': categories,
                                                           'comments': comments,
                                                           'form': form})


def journey_comments(request, journey_id):
    journey = Journey.objects.filter(id=journey_id).first()
    if not journey:
        raise Http404
    comments = Comment.objects.filter(journey=journey).exclude(is_published=False)
    form = CommentForm()
    categories = Category.objects.all()
    return render(request, 'product/journey_detail.html', {'journey': journey,
                                                           'comments': comments,
                                                           'form': form,
                                                           'categories': categories})


def create_comment(request, journey_id):
    if request.user.is_authenticated:
        journey = get_object_or_404(Journey, id=journey_id)
        if request.method == "POST":
            comment = Comment(body=request.POST['body'], journey=journey, user=request.user)
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                messages.success(request, _("Дякуємо за Ваш коментар. Опублікуємо після перевірки модератором!"))
                return redirect('/journey/{}/comments'.format(journey_id))
    else:
        return redirect('/')


def update_comment(request, comment_id, journey_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=comment_id, user=request.user.id)
        if request.method == "POST":
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('/journey/{}/comments'.format(journey_id))
        else:
            form = CommentForm(instance=comment)
        return render(request, 'product/journey_comments.html', {'form': form})
    else:
        return redirect('/')


def comment_delete(request, comment_id, journey_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=comment_id, user=request.user.id)
        if request.method == "POST":
            comment.delete()
            messages.error(extra_tags='danger', request=request, message=_('Ваш відгук видалено!'))
            return redirect('/journey/{}/comments'.format(journey_id))
        return render(request, "product/journey_comments.html")
    else:
        return redirect('/')


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    journeys = Journey.objects.filter(category=category)
    journeys_with_sale = Journey.objects.filter(category=category).exclude(sale_price__isnull=True)[:5]
    return render(request, 'product/Category_detail.html', {'category': category,
                                                            'categories': categories,
                                                            'journeys': handle_pagination(request, journeys),
                                                            'journeys_with_sale': journeys_with_sale})


def get_category_new(request):
    categories = Category.objects.all()
    journeys = Journey.objects.all()[:10]
    return render(request, 'product/new_journeys.html', {'categories': categories,
                                                         'journeys': journeys})


def get_category_sale(request):
    categories = Category.objects.all()
    journeys_with_sale = Journey.objects.exclude(sale_price__isnull=True)
    return render(request, 'product/sale_journeys.html', {'categories': categories,
                                                          'journeys_with_sale': journeys_with_sale})
