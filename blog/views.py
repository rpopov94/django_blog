from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    try:
        posts = Post.published.all()
    except Post.DoesNotExist:
        raise Http404('No Post found.')
    return render(
        request,
        'blog/posts/list.html',
        {'posts': posts}
    )


def post_detail(request, id):
    post = get_object_or_404(
        Post, id=id, status=Post.Status.PUBLISHED
    )
    return render(
        request,'blog/posts/detail.html', {'post': post}
    )
