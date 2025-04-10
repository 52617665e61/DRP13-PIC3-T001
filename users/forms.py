from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import NewUser

class formularioRegistroUsuario(UserCreationForm):
    '''#id = forms.
    email = forms.EmailField()
    primeiroNome = forms.CharField(max_length=30)
    ultimoNome = forms.CharField(max_length=30)
    contact = forms.CharField(max_length=16)

    class Meta:
        model = User
        fields = ('username', 'primeiroNome', 'ultimoNome', 'email', 'contact', 'password1', 'password2')'''
    
    
    class Meta:
        model = NewUser
        fields = ('email','user_name', 'first_name')

        labels = {
            
        }