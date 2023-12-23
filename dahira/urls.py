from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'dahira'

urlpatterns = [

    path('', views.dahira_view, name='dahira'),
    path('motdg/', views.dahiradetail_view, name='motdg'),
    path('success/', views.success, name='success'),
    path('erreur/', views.erreur, name='erreur'),



    # path('forms/', views.forms_view, name='forms'),
    




]
