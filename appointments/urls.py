from django.urls import path, include

from . import views
from rest_framework import routers
from appointments.views import AppointmentView
# router = routers.DefaultRouter()
# router.register('', views.AppointmentView, basename='appointments')

urlpatterns = [
    #path('', include(router.urls))
    path('', views.index, name="appointments"),
    path('get-appointment',
         AppointmentView.as_view({'get': 'list'}), name="get-appointment"),
    path('<int:appointment_id>', views.appointment, name="appointment")
]
