from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_dashboard, name='data_dashboard'),
    path('data', views.staff_data, name='staff_data'),
]
