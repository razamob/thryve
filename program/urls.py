from django.urls import path, include
from program import views
from rest_framework import routers
from program.views import SchoolProgramView
from program.views import SchoolProgramAPI
# router = routers.DefaultRouter()
# router.register(r'api-appointmentaccounts', views.StudentAccountAPI)

urlpatterns = [
    #path('', include(router.urls))
    path('', views.index, name="schoolprograms"),
    path('get-schoolprogram',
         SchoolProgramView.as_view({'get': 'list', 'post': 'create'}), name="get-schoolprogram"),
    path('find-schoolprogram/<int:id>',
         views.find_schoolprogram, name="find-schoolprogram")
]