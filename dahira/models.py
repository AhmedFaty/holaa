from django.db import models
from embed_video.fields import EmbedVideoField
from django_countries.fields import CountryField
# from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator




# Create your models here.

class Headerdahira(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(default='first_page1.jpg')

    def __str__(self) -> str:
        return self.titre
    

class MotDuDirecteur(models.Model):
    titre = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=150)
    contenu = models.TextField()
    image = models.ImageField(default='first_page1.jpg')

    def __str__(self) -> str:
        return self.titre
    

class DevenirMembreForm(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254)
    tel = PhoneNumberField()
    pays = CountryField(blank_label='(select country)')
    adresse = models.CharField(max_length=200)
