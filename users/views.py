
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
    

    """if request.method=="POST":
        form = formularioRegistroUsuario(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data['username']
            senha = form.cleaned_data['password1']
            user = authenticate(username=usuario, password=senha)
            login(request, user)
            return redirect('/')
    else:
        form = formularioRegistroUsuario()


    return render(request, 'registration/registroUsuario.html',{'form':form})
"""

'''class Perfil(UpdateView):
    template_name='refistration/perfil.html'
    model = Perfil
    fields = ['nome-completo', 'cpf']
    success_url = reverse_lazy('index')

    
    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
          context = super().get_context_data(*args, **kwargs)
          context['titulo'] = 'Meus dados'
          context['botao'] = 'Atualizar'
          return super().get_context_data'''

@login_required
def perfil(request):
    perfil = NewUser.objects.all().filter(id=request.user.id)
    registros= Appoitment.objects.all().filter(user=request.user.user_name)
    return render(request, 'registration/perfil.html', {'perfil':perfil, 'registros': registros}) 


