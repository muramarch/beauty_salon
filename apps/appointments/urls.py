from django.urls import path
from . import views

urlpatterns = [
    path('select-service/', views.select_service, name='select_service'),
    path('select-master/<int:service_id>/', views.select_master, name='select_master'),
    path('select-date/<int:service_id>/<int:master_id>/', views.select_date, name='select_date'),
    path('select_time/<int:service_id>/<int:master_id>/<str:selected_date>/', views.select_time, name='select_time'),
    # path('select-time-slot/<int:service_id>/<int:master_id>/<str:date>/', views.select_time_slot, name='select_time_slot'),
    # path('appointment-confirmation/', views.appointment_confirmation, name='appointment_confirmation'),
    # # Добавьте другие URL-пути для вашей системы записи на приемы, если необходимо
]
