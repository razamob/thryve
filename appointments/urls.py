from django.urls import path, include

from . import views
from rest_framework import routers
from appointments.views import AppointmentView
from appointments.views import AppointmentAPI
router = routers.DefaultRouter()
router.register(r'api-appointments', views.AppointmentAPI)

urlpatterns = [
    #path('', include(router.urls))
    path('', views.index, name="appointments"),
    path('get-appointment',
         AppointmentView.as_view({'get': 'list', 'post': 'create'}), name="get-appointment"),
    path(r'', include(router.urls)),
    path('<int:appointment_id>', views.appointment, name="appointment")
]
