from django.shortcuts import render, redirect
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.


def home(request):
    post_list = Article.objects.filter(post_type__in=['A', 'V', 'I', 'S', 'B'])  # 显示这些类型的post
    # post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'home.html', {'post_list': post_list})


def proj_home(request):
    post_list = Article.objects.filter(post_type__in=['P'])  # 显示这些类型的post
    # post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'proj.html', {'post_list': post_list})


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def detail_slug(request, slug):
    try:
        post = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list,
                                             'error': False})


def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            post_list = Article.objects.filter(title__icontains=s)
            if len(post_list) == 0:
                return render(request, 'archives.html', {'post_list': post_list,
                                                         'error': True})
            else:
                return render(request, 'archives.html', {'post_list': post_list,
                                                         'error': False})
    return redirect('/')


def about(request):
    try:
        post_about = Article.objects.get(slug='about')
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'about.html', {'post_about': post_about})


def search_tag(request, tag):
    post_list = Article.objects.filter(category__iexact=tag)  # contains
    if len(post_list) == 0:
        return render(request, 'tag.html', {'post_list': post_list, 'error': True})
    else:
        return render(request, 'tag.html', {'post_list': post_list, 'error': False, 'search_tag': tag})

