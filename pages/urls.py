from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('logout', views.logout, name="logout"),
    path('dashboard', views.dashboard, name="dashboard"),


    path('manageData', views.manage_data, name="manageData"),
    path('filterData', views.filter_data, name="filterData"),
    path('editmeetingcomments', views.edit_meeting_comments, name="editmeetingcomments"),
    # is it cus they had thesame name?
    path('filterDatachange', views.check_frequency, name="check-frequency"),
    #i may have to change the username of the below to manageData also
    path('managedata-table-load', views.table_load_up, name="managedata-table-load")

    #path('filterdatasearch', views.filter_data_search, name="filterdatasearch")
]
