from django.contrib import admin

from apps.masters.models import Master, MasterSchedule, WorkingDay

admin.site.register(WorkingDay)
admin.site.register(MasterSchedule)
admin.site.register(Master)