from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    # Existing URL patterns
    path('select_master/', views.select_master, name='select_master'),
    path('select_service/<int:master_id>/', views.select_service, name='select_service'),
    path('select_date/<int:service_id>/<int:master_id>/', views.select_date, name='select_date'),
    path('select_time/<int:service_id>/<int:master_id>/<str:selected_date>/', views.select_time, name='select_time'),
    # New URL pattern for booking the appointment
    path('book_appointment/<int:service_id>/<int:master_id>/<str:selected_date>/<str:selected_time>/', views.book_appointment, name='book_appointment'),
]
