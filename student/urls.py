from django.urls import path, include
from student import views
from rest_framework import routers
from student.views import StudentAccountView
from student.views import StudentAccountAPI
# router = routers.DefaultRouter()
# router.register(r'api-studentaccounts', views.StudentAccountAPI)

urlpatterns = [
    #path('', include(router.urls))
    path('', views.index, name="studentaccounts"),
    path('get-studentaccount',
         StudentAccountView.as_view({'get': 'list', 'post': 'create'}), name="get-studentaccount"),
    # path(r'', include(router.urls)),
    path('insert-studentaccount/<int:auth>/<int:prog>',
         views.insert_studentaccount, name="insert-studentaccount"),
    path('find-studentaccount/<int:id>',
         views.find_studentaccount, name="find-studentaccount"),
    path('delete-studentaccount/<int:id>',
         views.delete_studentaccount, name="delete-studentaccount"),
    path('edit-studentaccount/<int:id>/',
         views.edit_studentaccount, name="edit-studentaccount")
]