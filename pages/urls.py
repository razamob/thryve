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
    path('managedata-table-load', views.table_load_up, name="managedata-table-load"),
    path('managedata-table-row-delete', views.table_row_delete, name="managedata-table-row-delete"),
    path('managedata-table-row-add-load', views.table_row_add_capture_all, name="managedata-table-row-add-load"),
    path('managedata-table-deletion-queue-load', views.table_load_up_deletions, name="managedata-table-deletion-queue-load"),
    path('managedata-table_load_up_empty_notes', views.table_load_up_empty_staff_notes, name="managedata-table_load_up_empty_notes"),
    path('managedata_to_edit_page', views.managedata_table_row_to_edit_page, name="managedata_to_edit_page"),
    #put /<> to make it take '/' parameters when the view is called on. use "int:" to make the parameter only accept integers 
    path('editmeetingcomments/<int:id>', views.manageData_post_to_edit_meeting_comments, name='managedata-editmeetingcomments'),
    path('editmeeting_save_meeting_comments_page', views.editmeeting_save_meeting_comments, name='editmeeting_save_meeting_comments_page'),
    path('load_form_of_current_staff_on_filter_page', views.load_staff_forms_on_filterdata_page, name='load_form_of_current_staff_on_filter_page')
    #path('filterdatasearch', views.filter_data_search, name="filterdatasearch")
]
