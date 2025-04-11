from django.shortcuts import render, redirect
from .models import Appoitment
from .form import AppoitmentForm
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
            processo.user = request.user.first_name
            processo.save()
            return redirect('/')
    else:
        form = AppoitmentForm()
        return render(request, 'appoitments/appoitmentRegister.html', {'form': form})


