from django.db import models

from apps.appointments.models import Appointment

class Journal(models.Model):
    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE
    )
    status = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.appointment} - {self.action} - {self.appointment.date}"