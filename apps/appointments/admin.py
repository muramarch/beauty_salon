from django.contrib import admin

from .models import Appointment, ConfirmationCode

from django.contrib import admin
from apps.journal.models import Journal

class AppointmentAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        created = not obj.pk
        super().save_model(request, obj, form, change)

        action = "Created" if created else "Updated"
        entry = Journal(appointment=obj, action=action)
        entry.save()

admin.site.register(Appointment, AppointmentAdmin)

admin.site.register(ConfirmationCode)

# Register your models here.
