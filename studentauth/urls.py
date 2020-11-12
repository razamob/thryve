from django.urls import path, include
from studentauth import views
from rest_framework import routers
from studentauth.views import StudentAuthView
from studentauth.views import StudentAuthAPI
# router = routers.DefaultRouter()
# router.register(r'api-appointmentaccounts', views.StudentAccountAPI)

urlpatterns = [
    #path('', include(router.urls))
    path('', views.index, name="studentauths"),
    path('get-studentauth',
         StudentAuthView.as_view({'get': 'list', 'post': 'create'}), name="get-studentauth"),
    # path(r'', include(router.urls)),
    path('delete-studentauth/<int:id>',
         views.delete_studentauth, name="delete-studentauth"),
    path('edit-studentauth/<int:id>/',
         views.edit_studentauth, name="edit-studentauth")
]