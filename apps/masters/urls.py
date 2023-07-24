from django.urls import path
from django.contrib.auth import views
from apps.masters.views import CustomLoginView, CustomLogoutView, master_account

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name='masters/master-login.html'), name='master-login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('master-account/', master_account, name='master-account'),
]
