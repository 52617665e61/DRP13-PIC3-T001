from django.shortcuts import render, redirect
from .models import Service
from .form import ServiceForm
from django.contrib.auth.decorators import login_required, user_passes_test

def servicesList(request):
    services = Service.objects.all().order_by('-id')
    return render(request, 'services/servicesList.html', {'services':services})

@user_passes_test(lambda u: u.is_superuser)
def addService(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            processo = form.save(commit=False)
            processo.save()
            return redirect('managerService')
    else:
        form = ServiceForm()
        return render(request, 'services/serviceRegister.html', {'form': form})

def updateService(request, id):
    register = Service.objects.get(id=id)
    form = ServiceForm(request.POST or None, request.FILES or None,instance=register)
    if form.is_valid():
        form.save()
        return redirect('managerService')
    return render(request, 'services/updateService.html', {'register': register, 
                                                         'form':form})

@user_passes_test(lambda u: u.is_superuser)
def delService(request, id):
    register = Service.objects.get(id=id)
    register.delete()
    return redirect('managerService')                                                        

@user_passes_test(lambda u: u.is_superuser)
def manager(request):
    services = Service.objects.all().order_by('-id')
    totalService = Service.objects.all().count()
    context = {
        'services':services, 
        'totalService':totalService
    }
    return render(request, 'services/managerService.html', context)

