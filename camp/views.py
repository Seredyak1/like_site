from django.shortcuts import render, get_object_or_404, redirect

from .models import Camp, CampComment
from product.models import Category
from .forms import CampCommentForm


def get_camp_page(request):
    categories = Category.objects.all()
    camps = Camp.object.all()
    return render(request, 'camp/home_camp_page.html', {'camps': camps,
                                                        'categories': categories})


def get_camp_detail(request, slug):
    categories = Category.objects.all()
    camp = get_object_or_404(Camp, slug=slug)
    camp_comments = camp.comments_camp.all()
    form = CampCommentForm()
    return render(request, 'camp/camp_detail.html', {'camp': camp,
                                                     'categories': categories,
                                                     "camp_comments": camp_comments,
                                                     "form": form})


def camp_create_comment(request, slug):
    if request.user.is_authenticated:
        camp = get_object_or_404(Camp, slug=slug)
        if request.method == "POST":
            camp_comment = CampComment(body=request.POST['body'], camp=camp, user=request.user)
            form = CampCommentForm(request.POST, instance=camp_comment)
            if form.is_valid():
                form.save()
                return redirect('/camps/{}/'.format(slug))
    else:
        return redirect('/')


def camp_update_comment(request, с_id, slug):
    if request.user.is_authenticated:
        camp_comment = get_object_or_404(CampComment, id=с_id, user=request.user.id)
        if request.method == "POST":
            form = CampCommentForm(request.POST, instance=camp_comment)
            if form.is_valid():
                form.save()
                return redirect('/camps/{}/'.format(slug))
        else:
            form = CampCommentForm(instance=camp_comment)
        return render(request, 'camp/camp_comments.html', {'form': form})
    else:
        return redirect('/')


def camp_comment_delete(request, с_id, slug):
    if request.user.is_authenticated:
        camp_comment = get_object_or_404(CampComment, id=с_id, user=request.user.id)
        if request.method == "POST":
            camp_comment.delete()
            return redirect('/camps/{}/'.format(slug))
        return render(request, "camp/camp_comments.html")
    else:
        return redirect('/')