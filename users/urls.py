from django.urls import path, include
from . import views
from .views import RegistroUsuario, perfil


urlpatterns=[
    path('registroUsuario', RegistroUsuario.as_view(), name='registroUsuario'),
    path('perfil', views.perfil, name='perfil'),
    path('weather', views.weather, name='weather'),
    path('analisy', views.analisy, name='analisy')
   
    ]