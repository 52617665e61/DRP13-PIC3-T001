from django.shortcuts import render, redirect
from .models import Appoitment
from .form import AppoitmentForm


def appoitmentsList(request):
    appoitments = Appoitment.objects.all().order_by('-id')
    return render(request, 'appoitments/appoitmentsList.html', {'appoitments': appoitments})



def addAppoitment(request):
    if request.method == 'POST':
        form = AppoitmentForm(request.POST, request.FILES)
        if form.is_valid():
            processo = form.save(commit=False)
            processo.user = request.user.id
            processo.save()
            return redirect('/')
    else:
        form = AppoitmentForm()
        return render(request, 'appoitments/appoitmentRegister.html', {'form': form})
