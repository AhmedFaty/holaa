from django.contrib import admin


from .models import HeaderDjimThiam, BiblioDjimThiam, VideoBayeNena, HeaderNdaguaSarr, BiblioNdaguaSarr, VideoNdaguaSarr, HeaderEtoileDeLaFayda, HommageOustazAhmedBa, Post


# Register your models here.

admin.site.register(HeaderDjimThiam)

admin.site.register(BiblioDjimThiam)


@admin.register(VideoBayeNena)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titre', "desc")

########################################################################

admin.site.register(HeaderNdaguaSarr)

admin.site.register(BiblioNdaguaSarr)


@admin.register(VideoNdaguaSarr)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titre', "desc")


########################################################################

admin.site.register(HeaderEtoileDeLaFayda)
admin.site.register(HommageOustazAhmedBa)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titre', 'status', 'date_published')
    prepopulated_fields = {'slug': ('titre',)}
    search_fields = ('titre', 'status')

