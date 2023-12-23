from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,)
from django.shortcuts import render, get_object_or_404

from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings


from .models import *
from .forms import ContactForm



def home_view(request):
    teams = Teams.objects.all()
    posts = Biblio.objects.all()
    madrassa = Madrassa.objects.all()
    soufis = PlumeSoufis.objects.all()
    holaa = Outaz_biblio.objects.all()
    form = ContactForm()

    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         nom = request.POST['nom']
    #         email = request.POST['email']
    #         tel = request.POST['tel']
    #         message = request.POST['message']

    #         titre = f'Blog | {nom}  {email}  {tel}'
    #         send_mail(titre, message, 
    #                   settings.EMAIL_HOST_USER,
    #                   ['holaadahiratoul@gmail.com'],
                      
    #                 fail_silently= False)


        # return HttpResponseRedirect(reverse('remerciement'))

    context= {
        'posts': posts,
        'teams': teams,
        'madrassa': madrassa,
        'soufis': soufis,
        'form': form,
        'holaa': holaa,

    }
    return render(request, "home/home.html", context)


def remerciement_view(request):
    return HttpResponse("Merci de nous avoir contacté")


def biblio_view(request):
    # biblio = get_object_or_404(Biblio, slug=slug)
    biblio = get_object_or_404(Biblio)
    return render(request, 'home/biblio.html', context={'biblio': biblio})

def teams_view(request, slug_team):
    teams = Teams.objects.get(slug=slug_team)
    return render(request, 'home/teams.html', context={'teams': teams})
    
def madrassa_view(request, slug_madrassa):
    madrassa = Madrassa.objects.get(slug=slug_madrassa)
    return render(request, 'home/madrassa.html', context={'madrassa': madrassa})

def soufis_view(request, slug_soufis):
    soufis = PlumeSoufis.objects.get(slug=slug_soufis)
    return render(request, 'home/soufis.html', context={'soufis': soufis})
