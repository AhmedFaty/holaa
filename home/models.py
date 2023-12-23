from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Category(models.Model):
    name = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=200)
    
    def __str__(self):
        return self.name

class Article(models.Model):
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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted')
    
    objects = models.Manager() # Default Manager
    published = PublishedManager() # Custom Manager

    def __str__(self) -> str:
        return self.titre
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre + "-" + str(self.date_published))
        return super().save(*args, **kwargs)
    

class Biblio(models.Model):
    titre = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=150)
    contenu = models.TextField()
    image = models.ImageField(default='first_page1.jpg')

    def __str__(self) -> str:
        return self.titre



class Teams(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=150)
    contenu = models.TextField()
    image = models.ImageField(default='first_page1.jpg')
    # added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.titre
    


class Madrassa(models.Model):
    # grand_titre = models.CharField(max_length=200)
    # resumer = models.CharField(max_length=200)
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=150)
    contenu = models.TextField()
    image = models.ImageField(default='first_page1.jpg')

    def __str__(self) -> str:
        return self.titre
    

class PlumeSoufis(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    contenu = models.TextField()
    image = models.ImageField(default='first_page1.jpg')

    def __str__(self) -> str:
        return self.titre
    
    
class HeaderAricle(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(default='first_page1.jpg')

    def __str__(self) -> str:
        return self.titre


class Outaz_biblio(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()

    def __str__(self) -> str:
        return self.titre



