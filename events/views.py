from django.shortcuts import render
from django.core import serializers

from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,)


# Create your views here.
from .models import Event, HeaderEvent, Video

def events_view(request):
    events = Event.objects.all()
    header = HeaderEvent.objects.all()
    video = Video.objects.all().order_by('-added')
    paginator = Paginator(video, 3)
    page = request.GET.get('page')
    try:
        video = paginator.page(page)
    except PageNotAnInteger:
        video = paginator.page(1)
    except EmptyPage:
        video = paginator.page(paginator.num_pages)

    event_data = serializers.serialize('json', events)

    context = {
        'event_data': event_data,
        'header': header,
        'video': video,
    }
    
    return render(request, 'events/events.html', context)