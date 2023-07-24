from django.urls import path

from apps.core.views import indexView

urlpatterns = [
    path('', indexView, name='index'),
]
