from django.shortcuts import render, redirect
from apps.appointments.forms import AddAppointmentForm
from apps.masters.models import Master
from .models import Appointment
from apps.clients.models import Client

def add_appointment(request):
    appointment_created = False
    masters = Master.objects.all()

    if request.method == 'POST':
        form = AddAppointmentForm(request.POST)

        if form.is_valid():
            master = form.cleaned_data['master']  # Get the Master object, not just the ID
            service = form.cleaned_data['service']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            client_name = form.cleaned_data['client_name']
            client_phone_number = form.cleaned_data['client_phone_number']

            # Проверка, существует ли клиент в db
            client, created = Client.objects.get_or_create(
                name=client_name,
                phone_number=client_phone_number
            )

            # Создание записи на услугу
            appointment = Appointment.objects.create(
                client=client,
                master=master,
                service=service,
                date=date,
                description=description
            )

            appointment_created = True
    else:
        form = AddAppointmentForm()

    return render(request, 'appointments/appointment.html', {
        'form': form,
        'appointment_created': appointment_created,
        'masters': masters,
    })
