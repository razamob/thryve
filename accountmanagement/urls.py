from django.urls import path, include
from . import views
from rest_framework import routers
from appointments.views import AppointmentView
from appointments.views import AppointmentAPI
# router = routers.DefaultRouter()
# router.register(r'api-appointments', views.AppointmentAPI)

urlpatterns = [
    #path('', include(router.urls))
    path('', views.index, name="account"),
    path('get-account',
         AppointmentView.as_view({'get': 'list', 'post': 'create'}), name="get-account"),
    # path(r'', include(router.urls)),
    path('update-account',
         views.update_account, name="update-account")
]
