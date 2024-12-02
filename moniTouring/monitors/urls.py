from django.urls import path
from .views import *


urlpatterns = [
    path('add/', monitor_add, name="monitor add"),
    path('details/<slug:monitor_name>/', monitor_details, name="monitor details"),
    path('edit/<slug:monitor_name>/', monitor_edit, name="monitor edit"),
    path('delete/<slug:monitor_name>/', monitor_delete, name="monitor delete"),
]