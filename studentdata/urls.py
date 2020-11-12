from django.urls import path, include
from . import views
from rest_framework import routers
from studentdata.views import StudentDataView
from studentdata.views import StudentDataAPI

urlpatterns = [
    #path('', include(router.urls))
    path('', views.index, name="studentdatas"),
    path('get-studentdata',
         StudentDataView.as_view({'get': 'list', 'post': 'create'}), name="get-studentdata"),
    # path(r'', include(router.urls)),
    path('delete-studentdata/<int:id>',
         views.delete_studentdata, name="delete-studentdata"),
    path('edit-studentdata/<int:id>/',
         views.edit_studentdata, name="edit-studentdata")
]
