from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('health_workers', views.healthworkers, name='health-workers'),
    path('create_health_worker', views.create_health_worker, name='create-heath-worker'),
    path('delete_health_worker/<int:pk>', views.delete_healthworker, name='delete-health-worker'),
    path('edit_health_worker/<int:pk>', views.edit_health_worker, name='edit-health-worker'),
    path('view_my_report/<int:id>', views.view_report, name='view-report'),
    path('view_hw/<int:id>', views.view_hw, name='view-health-worker'),

    path('dash2', views.dash2, name='dash2'),
    # profile and report  section
    path('profile', views.profile, name='profile'),
    path('report', views.data_entry, name='report'),
    path('my_reports', views.my_reports, name='my-reports'),
    path('details', views.details, name='details'),
    path('sendsms/<int:id>', views.sendsms, name='sendsms'),
    path('delete_report/<int:id>', views.delete_report, name='delete-report'),
    path('edit_report/<int:id>', views.edit_report, name='edit-report'),
    

    # visuliazation urls
    path('visualization/<str:dist_name>', views.visualization, name='visualization'),
    

    ]
