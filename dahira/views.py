from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect


from .forms import *

from .models import *


def dahira_view(request):
    header = Headerdahira.objects.all()
    motdirecteur = MotDuDirecteur.objects.all()
    # message =  ""
    # video = VideoBayeNena.objects.all().order_by('-added')
    form = FormMembre()
    if request.method == 'POST':
        form = FormMembre(request.POST)

        if form.is_valid():
            tel = form.save(commit=False)
            form.save()
            return render (request, 'dahira/success.html', {'header': header})
        else:
            return render (request, 'dahira/erreur.html', {'header': header})
        
        
    # form = FormMembre(request.POST)
    # return render(request, 'dahira/dahira.html', {'form': form})


        # form.save()
        # return HttpResponseRedirect ('/dahira')
        # form.save()
        # return HttpResponseRedirect ('/dahira')


    context = {
        'header': header,
        'motdirecteur': motdirecteur,
        'form': form,


    }
    
    return render(request, 'dahira/dahira.html', context)



def success(request):
    return render(request, 'dahira/success.html')
def erreur(request):
    return render(request, 'dahira/erreur.html')



def dahiradetail_view(request):
    fayda= get_object_or_404(MotDuDirecteur)
    return render(request, 'dahira/dahiradetail.html', context={'fayda': fayda})


