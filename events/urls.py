from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'events'

urlpatterns = [

    path('', views.events_view, name='events'),
    path('<slug:slug>/', views.events_view, name='events'),


]
