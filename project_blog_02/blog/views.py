from django.shortcuts import render
from django.http import Http404

def index(request):
    template = 'blog/index.html'
    context = {'posts': posts[::-1]}
    return render(request, template, context)


def post_detail(request, post_id):
    if POSTS[post_id] is None:
        raise Http404('ТАКОГО ПОСТА НЕ СУЩЕСТВУЕТ')
    template = 'blog/detail.html'
    context = {'post': POSTS[post_id]}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'posts': category_slug}
    return render(request, template, context)
