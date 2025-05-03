from django.shortcuts import render, redirect
from .models import Appoitment
from .form import AppoitmentForm, UpdateAppoitmentForm
from django.contrib.auth.decorators import login_required, user_passes_test
from users.models import NewUser
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse

import logging

logger = logging.getLogger(__name__)




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

            logger.debug(f"Processo de agendamento para a data {processo.date} e hora {processo.hour}")

            consult_appoitments = Appoitment.objects.all().filter(date = processo.date)
            taken_hours = [t.hour.strftime('%H:%M') for t in consult_appoitments]

            logger.debug(f"Horários já ocupados: {taken_hours}")

            if processo.hour.strftime('%H:%M') in taken_hours:
                # Se o horário estiver ocupado, renderiza o form novamente com o erro
                return render(request, 'appoitments/appoitmentRegister.html', {'form': form, 'alert': True})
            processo.user = request.user.user_name
            processo.name = f"{request.user.first_name} {request.user.last_name}"
            processo.save()

            logger.info("Agendamento salvo com sucesso!")

            request.session['alert'] = True
            return redirect('perfil')
        else:
            return render(request, 'appoitments/appoitmentRegister.html', {'form': form})
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


def get_available_hours(request):
    date = request.GET.get('date')
    if not date:
        return JsonResponse({'hours': []})

    existing_appointments = Appoitment.objects.filter(date=date)
    taken_hours = set(a.hour.strftime('%H:%M') for a in existing_appointments)

    all_hours = [f"{h:02d}:00" for h in range(8, 19)]  # de 08:00 até 18:00
    available_hours = [hour for hour in all_hours if hour not in taken_hours]

    return JsonResponse({'hours': available_hours})