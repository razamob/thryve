from django.urls import path, include
from appointments import views
from rest_framework import routers
from appointments.views import AppointmentView
from appointments.views import AppointmentAPI
# router = routers.DefaultRouter()
# router.register(r'api-appointments', views.AppointmentAPI)

urlpatterns = [
    #path('', include(router.urls))
    path('', views.index, name="appointments"),
    path('get-appointment',
         AppointmentView.as_view({'get': 'list', 'post': 'create'}), name="get-appointment"),
    # path(r'', include(router.urls)),
    path('list-user-appointments/<int:student_num>',
          views.list_user_appointments, name="list-user-appointment"),
    path('list-day-appointments/<int:staff>/<int:y>/<int:m>/<int:d>',
          views.list_day_appointments, name="list-day-appointment"),
    path('insert-appointment/<int:cc>/<int:ec>/<int:staf>/<int:stud>',
         views.insert_appointment, name="insert-appointment"),
    path('delete-appointment/<int:id>',
         views.delete_appointment, name="delete-appointment"),
    path('delete-mobile-appointment/<int:id>',
         views.delete_mobile_appointment, name="delete-mobile-appointment"),
    path('edit-appointment/<int:id>/',
         views.edit_appointment, name="edit-appointment")
]
