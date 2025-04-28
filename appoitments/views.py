from django.shortcuts import render, redirect
from .models import Appoitment
from .form import AppoitmentForm, UpdateAppoitmentForm
from django.contrib.auth.decorators import login_required, user_passes_test
from users.models import NewUser
from django.utils import timezone
from django.urls import reverse, reverse_lazy




@user_passes_test(lambda u: u.is_superuser)
def appoitmentsList(request):
    appoitments = Appoitment.objects.all().order_by('-id')
    return render(request, 'appoitments/appoitmentsList.html', {'appoitments': appoitments})


@login_required
def addAppoitment(request, alert=False):
    if request.method == 'POST':
        form = AppoitmentForm(request.POST, request.FILES)
        if form.is_valid():
            processo = form.save(commit=False)
            consult_appoitments = Appoitment.objects.all().filter(date = processo.date)
            if len(consult_appoitments) > 0:
               for appoitment in consult_appoitments:
                    if processo.hour == appoitment.hour:
                        return render(request, 'appoitments/appoitmentRegister.html', {'form':form, 'alert':True})
            processo.user = request.user.user_name
            processo.name = [request.user.first_name, request.user.last_name]
            processo.save()
            request.session['alert'] = True
            return redirect('perfil')
    else:
        form = AppoitmentForm()
        return render(request, 'appoitments/appoitmentRegister.html', {'form': form})
   


@login_required
def info(request, id):
    info = Appoitment.objects.all().filter(id=id)
    return render(request, 'appoitments/info.html', {'info': info})

@user_passes_test(lambda u: u.is_superuser)
def updateAppoitment(request, id):
    register = Appoitment.objects.get(id=id)
    form = UpdateAppoitmentForm(request.POST or None, request.FILES or None,instance=register)
    if form.is_valid():
        form.save()
        return redirect('appoitmentsList')
    return render(request, 'appoitments/updateAppoitment.html', {'register': register, 
                                                         'form':form})


