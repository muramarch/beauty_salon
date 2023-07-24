from django import forms
from .models import Appointment, Master

class AddAppointmentForm(forms.ModelForm):
    # Добавьте поля для имени и номера телефона клиента
    client_name = forms.CharField(label='Имя клиента', max_length=255)
    client_phone_number = forms.CharField(label='Номер телефона клиента', max_length=20)
    master = forms.ModelChoiceField(queryset=Master.objects.all(), empty_label="Выберите мастера")

    class Meta:
        model = Appointment
        fields = (
            'service',
            'date',
            'description',
        )
