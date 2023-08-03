from django import forms
from apps.services.models import Service
from apps.masters.models import Master
from apps.clients.models import Client


class ServiceForm(forms.Form):
    service = forms.ModelChoiceField(queryset=Service.objects.all(), label='Выберите услугу')


class MasterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        selected_service = kwargs.pop('selected_service', None)
        super(MasterForm, self).__init__(*args, **kwargs)
        if selected_service:
            self.fields['master'].queryset = Master.objects.filter(service=selected_service)

    master = forms.ModelChoiceField(queryset=Master.objects.all(), label='Выберите мастера', widget=forms.RadioSelect)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone_number']
