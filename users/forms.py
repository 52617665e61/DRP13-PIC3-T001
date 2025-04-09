from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class formularioRegistroUsuario(UserCreationForm):
    #id = forms.
    email = forms.EmailField()
    primeiroNome = forms.CharField(max_length=30)
    ultimoNome = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'primeiroNome', 'ultimoNome', 'email', 'password1', 'password2')