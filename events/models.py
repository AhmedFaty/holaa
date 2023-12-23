from django.db import models
from embed_video.fields import EmbedVideoField



class Event(models.Model):
    name = models.CharField(max_length=200)
    event_date = models.DateField(auto_now_add=False)
    description = models.TextField()
    time = models.TimeField(auto_now=False)
    type = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class HeaderEvent(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(default='first_page1.jpg')

    def __str__(self) -> str:
        return self.titre
    
class Video(models.Model):
    url = EmbedVideoField()  # same like models.URLField()
    titre = models.CharField(max_length=200)
    desc = models.CharField(max_length=250)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.titre