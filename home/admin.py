from django.contrib import admin

from .models import *
from mediatheque.models import HeaderMedia, Video


# Articles
@admin.register(Article)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titre', 'status', 'date_published')
    prepopulated_fields = {'slug': ('titre',)}
    search_fields = ('titre', 'contenu')

admin.site.register(HeaderAricle)

admin.site.register(Outaz_biblio)



#Mediatheque
admin.site.register(HeaderMedia)

admin.site.register(Video)

#Homepage
admin.site.register(Biblio)

@admin.register(PlumeSoufis)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titre',)}

@admin.register(Madrassa)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titre',)}

@admin.register(Teams)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titre',)}