from django.shortcuts import render, redirect
from users.models import NewUser


def index(request):
    user_log = NewUser.objects.get(user_name=user_name)
    return render(request, 'tasks/index.html')

def home(request):
    return render(request, 'tasks/home.html')




