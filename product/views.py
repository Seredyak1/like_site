from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm, Comment
from .models import Journey
from django.http import Http404
from product.models import Category, Journey
from product.utils import handle_pagination


def journey_details(request, journey_id):
    journey = Journey.objects.filter(id=journey_id).first()
    if not journey:
        raise Http404

    return render(request, 'product/item_details.html', {'journey': journey})


def journey_comments(request, journey_id):
    journey = Journey.objects.filter(id=journey_id).first()
    if not journey:
        raise Http404
    comments = Comment.objects.filter(journey=journey)
    form = CommentForm()

    return render(request, 'product/item_details.html', {'journey': journey, 'comments': comments, 'form': form})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    journeys = Journey.objects.filter(category=category)
    journeys_with_sale = Journey.objects.filter(category=category).exclude(sale_price__isnull=True)[:5]
    return render(request, 'product/Category_detail.html', {'category': category,
                                                            'categories': categories,
                                                            'journeys': handle_pagination(request, journeys),
                                                            'journeys_with_sale': journeys_with_sale})


def create_comment(request, journey_id):
    if request.user.is_authenticated:
        journey = get_object_or_404(Journey, id=journey_id)
        if request.method == "POST":
            comment = Comment(body=request.POST['body'], journey=journey, user=request.user)
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('/journey/{}'.format(journey_id))
    else:
        return redirect('/')


def update_comment(request, comment_id, journey_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=comment_id, user=request.user.id)
        if request.method == "POST":
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('/journey/{}'.format(journey_id))
        else:
            form = CommentForm(instance=comment)
        return render(request, 'product/item_details.html', {'form': form})
    else:
        return redirect('/')


def comment_delete(request, comment_id, journey_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=comment_id, user=request.user.id)
        if request.method == "POST":
            comment.delete()
            return redirect('/journey/{}'.format(journey_id))
        return render(request, "product/item_details.html")
    else:
        return redirect('/')
