from django.urls import path
from . import views


urlpatterns = [
    path('create-appointment/', views.add_appointment, name='create-appointment'),
]
