from django.shortcuts import render, redirect
from users.models import NewUser
from django.contrib.auth.decorators import login_required, user_passes_test


def index(request):
    user_log = NewUser.objects.get(user_name=user_name)
    return render(request, 'tasks/index.html')

def home(request):
    return render(request, 'tasks/home.html')

@login_required
def homeUser(request):
    return render(request, 'tasks/homeUser.html')

@user_passes_test(lambda u: u.is_superuser)
def homeAdmin(request):
    return render(request, 'tasks/homeAdmin.html')






