from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



# OUSTAZ DJIM THIAM

class HeaderDjimThiam(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(default='first_page1.jpg')

    def __str__(self) -> str:
        return self.titre
    

class BiblioDjimThiam(models.Model):
    titre = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=150)
    contenu = models.TextField()
    image = models.ImageField(default='first_page1.jpg')

    def __str__(self) -> str:
        return self.titre
    

class VideoBayeNena(models.Model):
    url = EmbedVideoField()  # same like models.URLField()
    titre = models.CharField(max_length=200)
    desc = models.CharField(max_length=250)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.titre
    


# OUSTAZ NGDAGUA SARR

class HeaderNdaguaSarr(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(default='first_page1.jpg')

    def __str__(self) -> str:
        return self.titre
    

class BiblioNdaguaSarr(models.Model):
    titre = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=150)
    contenu = models.TextField()
    image = models.ImageField(default='first_page1.jpg')

    def __str__(self) -> str:
        return self.titre
    

class VideoNdaguaSarr(models.Model):
    url = EmbedVideoField()  # same like models.URLField()
    titre = models.CharField(max_length=200)
    desc = models.CharField(max_length=250)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.titre
    

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name= "category_posts")
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    slug = models.SlugField(max_length=200, null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg')
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=10)
    
    objects = models.Manager() # Default Manager
    published = PublishedManager() # Custom Manager

    def __str__(self) -> str:
        return self.titre
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre + "-" + str(self.date_published))
        return super().save(*args, **kwargs)
    


class HeaderEtoileDeLaFayda(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(default='first_page1.jpg')

    def __str__(self) -> str:
        return self.titre
    

class HommageOustazAhmedBa(models.Model):
    titre = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=150)
    contenu = models.TextField()
    image = models.ImageField(default='first_page1.jpg')

    def __str__(self) -> str:
        return self.titre