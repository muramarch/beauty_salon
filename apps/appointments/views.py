from datetime import timedelta, datetime, time
import datetime
from django.utils import timezone
from django.shortcuts import render, redirect

from apps.appointments.forms import ClientForm, MasterForm, ServiceForm
from apps.appointments.models import Appointment
from apps.masters.models import Master
from apps.services.models import Service


def select_master(request):
    if request.method == 'POST':
        form = MasterForm(request.POST)
        if form.is_valid():
            master_id = form.cleaned_data['master'].id
            return redirect('appointments:select_service', master_id=master_id)
    else:
        form = MasterForm()
    return render(request, 'appointments/select_master.html', {'master_form': form})


def select_service(request, master_id):
    selected_master = Master.objects.get(pk=master_id)

    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service_id = form.cleaned_data['service'].id
            return redirect('appointments:select_date', service_id=service_id, master_id=master_id)
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

    # Получаем выбранную дату из URL и преобразуем ее в объект типа datetime.date
    selected_date = timezone.datetime.strptime(selected_date, "%Y-%m-%d").date()

    # Получаем график работы мастера
    master_schedule = selected_master.schedule

    # Получаем рабочий день для выбранной даты
    working_day = master_schedule.working_days.filter(day_of_week=selected_date.weekday() + 1).first()

    # Если для выбранной даты нет рабочего дня, возвращаем сообщение об ошибке или перенаправляем на страницу ошибки
    if not working_day:
        return render(request, 'appointments/no_working_day.html', {
            'selected_service': selected_service,
            'selected_master': selected_master,
            'selected_date': selected_date
        })

    # Рассчитываем начальное и конечное время для выбранной даты
    start_time = timezone.datetime.combine(selected_date, working_day.start_time)
    end_time = timezone.datetime.combine(selected_date, working_day.end_time)

    # Рассчитываем продолжительность выбранной услуги
    service_duration = selected_service.duration

    # Рассчитываем доступные временные интервалы для выбранной даты (хранить в виде объектов типа datetime.time)
    available_time_slots = []
    while start_time + timedelta(minutes=service_duration) <= end_time:
        available_time_slots.append(start_time.time())
        start_time += timedelta(minutes=service_duration)

    if request.method == 'POST':
        # Обрабатываем отправку формы для выбора времени
        # Проверяем, что поле 'selected_time' присутствует в POST-запросе
        if 'selected_time' in request.POST:
            selected_time = request.POST['selected_time']
        else:
            selected_time = None  # или установите значение по умолчанию, например, selected_time = ""

        return redirect('appointments:book_appointment', service_id=service_id, master_id=master_id, selected_date=selected_date, selected_time=selected_time)

    return render(request, 'appointments/select_time.html', {
        'selected_service': selected_service,
        'selected_master': selected_master,
        'selected_date': selected_date,
        'available_time_slots': available_time_slots
    })
    
    
def book_appointment(request, service_id, master_id, selected_date, selected_time):
    selected_service = Service.objects.get(pk=service_id)
    selected_master = Master.objects.get(pk=master_id)

    # Парсим selected_date из строки URL и преобразуем его в объект datetime.date
    selected_date = datetime.datetime.strptime(selected_date, "%Y-%m-%d").date()

    # Если selected_time равен строке 'None' (например, при GET запросе), устанавливаем его равным None
    if selected_time == 'None':
        selected_time = None
    else:
        # Если selected_time не пустой строкой, конвертируем его в объект datetime.time
        selected_time = datetime.datetime.strptime(selected_time, "%H:%M").time()

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            # Save the client information to the database
            client = form.save()

            # Combine date and time into a single datetime value if selected_time is not None
            appointment_datetime = datetime.combine(selected_date, selected_time) if selected_time is not None else None

            # Save the appointment to the database
            appointment = Appointment.objects.create(
                client=client,
                service=selected_service,
                master=selected_master,
                date=appointment_datetime
            )

            # Perform any other actions related to the appointment (e.g., sending confirmation emails)

            return render(request, 'appointments/appointment_success.html', {
                'appointment': appointment,
                'selected_service': selected_service,
                'selected_master': selected_master,
                'selected_date': selected_date,
                'selected_time': selected_time,
            })
    else:
        form = ClientForm()

    return render(request, 'appointments/book_appointment.html', {
        'client_form': form,
        'selected_service': selected_service,
        'selected_master': selected_master,
        'selected_date': selected_date,
        'selected_time': selected_time,
    })

