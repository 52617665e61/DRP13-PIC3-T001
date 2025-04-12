from django.shortcuts import render, redirect
from .models import Appoitment
from .form import AppoitmentForm, UpdateAppoitmentForm
from django.contrib.auth.decorators import login_required, user_passes_test
from users.models import NewUser



@user_passes_test(lambda u: u.is_superuser)
def appoitmentsList(request):
    appoitments = Appoitment.objects.all().order_by('-id')
    return render(request, 'appoitments/appoitmentsList.html', {'appoitments': appoitments})


@login_required
def addAppoitment(request):
    if request.method == 'POST':
        form = AppoitmentForm(request.POST, request.FILES)
        if form.is_valid():
            processo = form.save(commit=False)
            processo.user = request.user.user_name
            processo.name = [request.user.first_name, request.user.last_name]
            processo.save()
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


