from django.urls import path, include
from . import views
from .views import RegistroUsuario, perfil


urlpatterns=[
    path('registroUsuario', RegistroUsuario.as_view(), name='registroUsuario'),
    path('perfil', views.perfil, name='perfil'),
   
    ]