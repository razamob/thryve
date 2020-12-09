from django.urls import path, include
from employmentform import views
from rest_framework import routers
from studentauth.views import EmploymentConsultantFormView
from studentauth.views import EmploymentConsultantFormAPI

urlpatterns = [
    #path('', include(router.urls))
    path('', views.index, name="employmentconsultantforms"),
    path('employmentconsultantform',
         EmploymentConsultantFormView.as_view({'get': 'list', 'post': 'create'}), name="get-employmentconsultantform"),
    # path(r'', include(router.urls)),
    path('delete-employmentconsultantform/<int:id>',
         views.delete_employmentconsultantform, name="delete-employmentconsultantform"),
    #path('edit-employmentconsultantform/<int:id>/',
    #     views.edit_employmentconsultantform, name="edit-employmentconsultantform")
]