from django.contrib import admin


from .models import Event, HeaderEvent, Video

# Events
@admin.register(Event)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_date', 'description', 'time')
    search_fields = ('name', 'event_date')

admin.site.register(HeaderEvent)

admin.site.register(Video)

