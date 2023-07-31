from django.urls import path
from . import views

urlpatterns = [
    path('select-master/', views.select_master, name='select_master'),
    path('select-service/<int:master_id>/', views.select_service, name='select_service'),

    path('select-date/<int:service_id>/<int:master_id>/', views.select_date, name='select_date'),
    path('select_time/<int:service_id>/<int:master_id>/<str:selected_date>/', views.select_time, name='select_time'),
]
