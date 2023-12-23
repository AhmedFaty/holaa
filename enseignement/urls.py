from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'enseignement'

urlpatterns = [

    path('', views.djimthiam_view, name='enseignement'),
    path('biblio/', views.biblio_view, name='biblio'),

    path('ndaguasarr/', views.ndaguasarr_view, name='ndaguasarr'),
    path('bibliosarr/', views.bibliosarr_view, name='bibliosarr'),

    path('hommage/', views.hommage_view, name='hommage'),


    path('fayda/', views.fayda_view, name='fayda'),
    path('<slug:slug>/', views.fayda_detail_view, name='article'),



   






]
