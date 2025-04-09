from django.shortcuts import render, redirect


def index(request):
    return render(request, 'tasks/index.html')

def home(request):
    return render(request, 'tasks/home.html')




