from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,)

from home.models import Article, Category, HeaderAricle


def articles_view(request, category=None):
    articles = Article.published.all().order_by('-date_published')
    categories = Category.objects.all()
    header = HeaderAricle.objects.all()
    if category:
        category = get_object_or_404(Category, slug=category)
        articles = articles.filter(category=category).order_by("publish")
    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context = {
        'articles': articles,
        'page': page,
        'categories': categories,
        'category': category,
        'header': header,
    }
    return render(request, 'articles/list.html', context)

def article_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles/detail.html', context={'article': article})
