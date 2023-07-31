from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, redirect

from apps.appointments.forms import MasterForm, ServiceForm
from apps.masters.models import Master
from apps.services.models import Service


def select_master(request):
    if request.method == 'POST':
        form = MasterForm(request.POST)
        if form.is_valid():
            master_id = form.cleaned_data['master'].id
            return redirect('select_service', master_id=master_id)
    else:
        form = MasterForm()
    return render(request, 'appointments/select_master.html', {'master_form': form})


def select_service(request, master_id):
    selected_master = Master.objects.get(pk=master_id)

    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service_id = form.cleaned_data['service'].id
            return redirect('select_date', service_id=service_id, master_id=master_id)
    else:
        # Фильтруем услуги на основе выбранного мастера
        available_services = Service.objects.filter(master=selected_master)
        form = ServiceForm()

    # Обновляем форму, чтобы она отображала только доступные услуги для выбранного мастера
    form.fields['service'].queryset = available_services

    return render(request, 'appointments/select_service.html', {
        'service_form': form,
        'selected_master': selected_master,
    })


def select_date(request, service_id, master_id):
    selected_service = Service.objects.get(pk=service_id)
    selected_master = Master.objects.get(pk=master_id)

    # Fetch the master's schedule, if it exists
    master_schedule = selected_master.schedule

    # Calculate the next 7 days starting from today
    today = timezone.now().date()
    next_seven_days = [today + timedelta(days=i) for i in range(7)]

    # Get the working days for the master
    working_days = []
    if master_schedule:
        working_days = master_schedule.working_days.all()

    # Filter the next 7 days to include only working days
    available_days = [day for day in next_seven_days if day.weekday() + 1 in [working_day.day_of_week for working_day in working_days]]

    return render(request, 'appointments/select_date.html', {
        'selected_service': selected_service,
        'selected_master': selected_master,
        'available_days': available_days
    })
    
    
def select_time(request, service_id, master_id, selected_date):
    selected_service = Service.objects.get(pk=service_id)
    selected_master = Master.objects.get(pk=master_id)

    # Get the selected date from the URL and convert it to a Python date object
    selected_date = timezone.datetime.strptime(selected_date, "%Y-%m-%d").date()

    # Fetch the master's schedule
    master_schedule = selected_master.schedule

    # Get the working day for the selected date
    working_day = master_schedule.working_days.filter(day_of_week=selected_date.weekday() + 1).first()

    # If there is no working day for the selected date, return an error message or redirect to an error page
    if not working_day:
        return render(request, 'appointments/no_working_day.html', {
            'selected_service': selected_service,
            'selected_master': selected_master,
            'selected_date': selected_date
        })

    # Calculate the start and end time for the selected date
    start_time = timezone.datetime.combine(selected_date, working_day.start_time)
    end_time = timezone.datetime.combine(selected_date, working_day.end_time)

    # Calculate the duration of the selected service
    service_duration = selected_service.duration

    # Calculate available time slots for the selected date
    available_time_slots = []
    while start_time + timedelta(minutes=service_duration) <= end_time:
        available_time_slots.append(start_time)
        start_time += timedelta(minutes=service_duration)

    return render(request, 'appointments/select_time.html', {
        'selected_service': selected_service,
        'selected_master': selected_master,
        'selected_date': selected_date,
        'available_time_slots': available_time_slots
    })