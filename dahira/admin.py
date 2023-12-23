from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Headerdahira)

admin.site.register(MotDuDirecteur)

# admin.site.register(DevenirMembreForm)




@admin.register(DevenirMembreForm)
class PostAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'tel', 'pays', 'adresse')


