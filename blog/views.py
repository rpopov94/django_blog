from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(
        request,
        'blog/posts/list.html',
        {'posts': posts}
    )


def post_detail(request, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post
    )

    return render(request,
                  'blog/posts/detail.html',
                  {'post': post})
