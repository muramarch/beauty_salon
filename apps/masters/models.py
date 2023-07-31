from django.contrib.auth.models import User
from django.db import models
from apps.services.models import Service

class WorkingDay(models.Model):
    day_of_week = models.PositiveIntegerField(choices=((1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')))
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.get_day_of_week_display()} ({self.start_time} - {self.end_time})"

class MasterSchedule(models.Model):
    master = models.ForeignKey('Master', on_delete=models.CASCADE, related_name='master_schedule')
    working_days = models.ManyToManyField(WorkingDay)

    def __str__(self):
        return f"Schedule for {self.master}"

class Master(models.Model):
    user = models.OneToOneField(User, related_name='user_master', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='master_photos')
    service = models.ManyToManyField(Service)
    schedule = models.OneToOneField(MasterSchedule, on_delete=models.CASCADE, null=True, blank=True, related_name='master_schedule')

    def __str__(self):
        return self.user.first_name
