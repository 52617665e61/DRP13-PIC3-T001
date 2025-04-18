
import datetime
import requests
from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import formularioRegistroUsuario
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import  NewUser
from appoitments.models import Appoitment
from django.conf import settings







##########################################################################################################################

# REGISTRO DE USUÁRIOS

##########################################################################################################################

class RegistroUsuario(CreateView):
    template_name ='registration/registroUsuario.html'
    form_class = formularioRegistroUsuario
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        
        return context
    
@login_required
def perfil(request, alert=False):
    alert = request.session.get('alert')
    perfil = NewUser.objects.all().filter(id=request.user.id)
    registros= Appoitment.objects.all().filter(user=request.user.user_name)
    return render(request, 'registration/perfil.html', {'perfil':perfil, 'registros': registros, 'alert':alert}) 

def weather(request):
    api_key = '0e4658549f8960c37a67ff75efa79522'
    city = request.GET.get('city', 'Dracena')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=pt&appid={api_key}'
    
    weather_data = {}
    error_message = None
    
    try:
        response = requests.get(url).json()

        if response.get('cod') !=200:
            raise ValueError(f"City '{city}' not found.")
        
        weather_data = {
            'city': city,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'humidity': response['main']['humidity'],
            'wind_speed': response['wind']['speed']
        }
    except ValueError as e:
        error_message = str(e)

    return render(request, 'registration/weather.html', {'weather_data': weather_data, 'error_message': error_message})
    
  




