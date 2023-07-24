from django.utils import timezone
from django.db import models
from apps.clients.models import Client
from apps.masters.models import Master
from apps.services.models import Service

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default='scheduled')

    def __str__(self):
        return f'Мастер: {self.master} - Услуга: {self.service} - Клиент: {self.client}'
    
    def save(self, *args, **kwargs):
        if self.date <= timezone.now():
            self.status = 'completed'
        super().save(*args, **kwargs)


class ConfirmationCode(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    expiration = models.DateTimeField()

    def __str__(self):
        return self.code