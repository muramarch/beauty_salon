from django.contrib import admin
from .models import Journal

class JournalAdmin(admin.ModelAdmin):
    readonly_fields = ('appointment', 'status', 'timestamp', 'action')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Journal, JournalAdmin)
