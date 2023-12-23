from django import forms
from .models import *
from django.forms import ModelForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.formfields import PhoneNumberField


class FormMembre(ModelForm):
    class Meta:
        model = DevenirMembreForm
        fields = ['nom', 'prenom', 'email', 'tel', 'pays', 'adresse']
  


        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'tel': forms.NumberInput(attrs={'class': 'form-control'} ),
            'pays': forms.Select(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),

        }

    tel = PhoneNumberField(
            widget= PhoneNumberPrefixWidget(initial= 'SN'),
            required = False,
            )
        





# class FormForm(forms.Form):
#     nom = forms.CharField()
#     prenom = forms.CharField()
#     adresse = forms.CharField()