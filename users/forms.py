from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import NewUser

class formularioRegistroUsuario(UserCreationForm):

    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'first_name', 'last_name', 'password1', 'password2')

        labels = {
            'email': 'E-mail',
            'user_name': 'Nome de usuário',
            'first_name' :'Nome',
            'last_name' :'Sobrenome',
            'password1' : 'Senha',
            'password2' : 'Repita a senha'
        }
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user