from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('articles/', include('articles.urls'), name='articles'),
    path('mediatheque/', include('mediatheque.urls'), name='mediatheque'),
    path('events/', include('events.urls'), name='events'),
    path('enseignement/', include('enseignement.urls'), name='enseignement'),
    path('dahira/', include('dahira.urls'), name='dahira'),






   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
