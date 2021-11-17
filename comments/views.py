from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse

from posts import forms, models as post_models
from . import models as comment_models
from . import forms


@login_required
def create_comment(request, post):

    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        post = get_object_or_404(post_models.Post, pk=post)
        if form.is_valid():
            comment = form.save()
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect(reverse("posts:detail", kwargs={"pk": post.pk}))
        else:
            raise Http404()


@login_required
def delete_comment(request, post, comment):

    post = get_object_or_404(post_models.Post, pk=post)
    comment = get_object_or_404(comment_models.Comment, pk=comment)
    comment.delete()
    return redirect(reverse("posts:detail", kwargs={"pk": post.pk}))
