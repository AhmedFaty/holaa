from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('biblio/', views.biblio_view, name='biblio'),
    path('teams/<str:slug_team>', views.teams_view, name='teams'),
    path('madrassa/<str:slug_madrassa>', views.madrassa_view, name='madrassa'),
    path('soufis/<str:slug_soufis>', views.soufis_view, name='soufis'),

    # path('remerciement/', views.remerciement_view, name='remerciement'),

    
    



]
