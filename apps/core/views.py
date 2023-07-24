from django.shortcuts import render

from apps.masters.models import Master

def indexView(request):
    masters = Master.objects.all()
    return render(request, 'core/index.html', {'masters': masters})