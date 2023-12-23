from django import forms


class ContactForm(forms.Form):
    nom = forms.CharField(
                          widget=forms.TextInput(
                              attrs={'class': 'name', 'placeholder': 'Votre nom et prenom' }
                          ))

    email = forms.EmailField(
                          widget=forms.TextInput(
                              attrs={'class': 'email', 'placeholder': 'Votre email'}
                          ))
    
    tel = forms.CharField(
                          widget=forms.TextInput(
                              attrs={'class': 'tel', 'placeholder': 'Votre nom et prenom'}
                          ))
    

    message = forms.CharField(
                        widget=forms.Textarea(
                            attrs={'class': 'message', 'placeholder': 'Votre message'}
                        ))
    


