from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,)




# Create your views here.
from .models import HeaderDjimThiam, BiblioDjimThiam, VideoBayeNena, HeaderNdaguaSarr, BiblioNdaguaSarr, VideoNdaguaSarr, Post, HeaderEtoileDeLaFayda, HommageOustazAhmedBa

def djimthiam_view(request):
    header = HeaderDjimThiam.objects.all()
    biblio = BiblioDjimThiam.objects.all()
    video = VideoBayeNena.objects.all().order_by('-added')

    paginator = Paginator(video, 3)
    page = request.GET.get('page')
    try:
        video = paginator.page(page)
    except PageNotAnInteger:
        video = paginator.page(1)
    except EmptyPage:
        video = paginator.page(paginator.num_pages)

    context = {
        'header': header,
        'biblio': biblio,
        'video': video,


    }
    
    return render(request, 'enseignement/djimthiam.html', context)


def biblio_view(request):
    biblio = get_object_or_404(BiblioDjimThiam)
    return render(request, 'enseignement/biblio.html', context={'biblio': biblio})



# OUSTAZ NDAGUA SARR


def ndaguasarr_view(request):
    header = HeaderNdaguaSarr.objects.all()
    biblio = BiblioNdaguaSarr.objects.all()
    video = VideoNdaguaSarr.objects.all().order_by('-added')

    paginator = Paginator(video, 3)
    page = request.GET.get('page')
    try:
        video = paginator.page(page)
    except PageNotAnInteger:
        video = paginator.page(1)
    except EmptyPage:
        video = paginator.page(paginator.num_pages)
        

    context = {
        'header': header,
        'biblio': biblio,
        'video': video,


    }
    
    return render(request, 'enseignement/ndaguasarr.html', context)


def bibliosarr_view(request):
    biblio= get_object_or_404(BiblioNdaguaSarr)
    return render(request, 'enseignement/bibliosarr.html', context={'biblio': biblio})


# ETOILES DE LA FADA 

def fayda_view(request, category=None):
    articles = Post.published.all().order_by('-date_published')
    header = HeaderEtoileDeLaFayda.objects.all()
    hommage = HommageOustazAhmedBa.objects.all()

    
    if category:
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
        'header': header,
        'hommage': hommage,

    }
    return render(request, 'enseignement/fayda.html', context)


def fayda_detail_view(request, slug):
    article = get_object_or_404(Post, slug=slug)
    return render(request, 'enseignement/faydadetail.html', context={'article': article})


def hommage_view(request):
    hommage= get_object_or_404(HommageOustazAhmedBa)
    return render(request, 'enseignement/hommagedetail.html', context={'hommage': hommage})