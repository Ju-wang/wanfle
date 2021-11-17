from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import EmptyPage, Paginator
from django.contrib import messages
from django.urls import reverse
from django.http import Http404

from posts import forms
from users import models as user_models
from comments import models as comment_models
from comments import forms as comment_forms

from . import models
from . import forms


def Home(request):
    # pep8
    return render(request, "posts/home.html")


def List(request):
    ott = request.GET.get('ott')
    page = request.GET.get('page', 1)
    # all_posts = models.Post.objects.all().order_by("-created")
    all_posts = models.Post.objects.filter(
        OttType__name=ott).order_by("-created")

    # select *
    # from post
    # inner join otttype ott on otttype.id = otttype.id
    # where ott.name = 'Netflix'
    paginator = Paginator(all_posts, 15, orphans=5)

    try:
        page_obj = paginator.get_page(page)

    except EmptyPage:
        return redirect("posts:list")
    return render(request, "posts/list.html", {
        "all_posts": all_posts,
        "pages": page_obj,
        "ott": ott
    })


def Detail(request, pk):

    form = comment_forms.CommentForm

    try:
        post = models.Post.objects.get(pk=pk)
        return render(request, "posts/detail.html", {"post": post, "form": form, })
    except models.Post.DoesNotExist:
        raise Http404()


@login_required
def Create_post(request):

    if request.method == "GET":
        form = forms.CreatePostForm()

    elif request.method == "POST":
        form = forms.CreatePostForm(request.POST)

        if form.is_valid():
            number_of_people = form.cleaned_data.get("number_of_people")
            if number_of_people >= 1 and number_of_people < 9:
                post = form.save(commit=False)
                post.host = request.user
                post.save()
                messages.success(request, "게시물이 생성되었습니다!")
                return redirect("posts:detail", pk=post.pk)
            else:
                return redirect("posts:create")

    return render(request, "posts/create.html", {"form": form})


# def create(request):
#     if request.method == "POST":
#         form = forms.CreatePostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.host = request.user
#             post.save()
#             return redirect("posts:detail", pk=post.pk)

#     form = forms.CreatePostForm()
#     return render(request, "posts/create.html", {"form": form})

@login_required
def Edit_post(request, pk):

    post = get_object_or_404(models.Post, pk=pk)

    # instance를 통해서 무엇을 수정할 것인지 정하게 해준다
    # 여기서는 get_object_or_404로 가져온 post를 사용했다
    if request.method == "GET":
        form = forms.CreatePostForm(instance=post)

    elif request.method == "POST":
        form = forms.CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            number_of_people = form.cleaned_data.get("number_of_people")
            if request.user == post.host:
                if number_of_people > 1 and number_of_people < 9:
                    post.save()
                    messages.success(request, "게시물이 수정되었습니다!")
                    return redirect("posts:detail", pk=post.pk)

    return render(request, "posts/edit.html", {"form": form, "post": post})


@login_required
def Delete(request, pk):
    ott = request.GET.get('ott')
    post = get_object_or_404(models.Post, pk=pk)
    post.delete()
    messages.error(request, "게시물이 삭제되었습니다!")
    return redirect("posts:list")
