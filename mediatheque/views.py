from django.shortcuts import render
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,)


from .models import Video, HeaderMedia


def mediavideo_view(request):
    video = Video.objects.all().order_by('-added')
    header = HeaderMedia.objects.all
    paginator = Paginator(video, 6)
    page = request.GET.get('page')
    try:
        video = paginator.page(page)
    except PageNotAnInteger:
        video = paginator.page(1)
    except EmptyPage:
        video = paginator.page(paginator.num_pages)


    context = {
    'video': video,
    'header': header,

    }

    return render(request, "mediatheque/media.html", context)
