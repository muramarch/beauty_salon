from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy

from apps.masters.models import Master
from apps.appointments.models import Appointment

class CustomLoginView(LoginView):
    template_name = 'masters/master-login.html'

    def get_success_url(self):
        return reverse_lazy('master-account')  # Замените 'your-template-name' на имя желаемого шаблона
    

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')


def master_account(request):
    master = Master.objects.get(user=request.user)  # Assuming you want to get the master profile for the currently logged-in user.
    appointments = Appointment.objects.filter(master=master)
    appointments_count = appointments.count()
    return render(request, 'masters/master-account.html', {
        'master': master,
        'appointments': appointments,
        'appointments_count': appointments_count
    })
    


        
        


    
