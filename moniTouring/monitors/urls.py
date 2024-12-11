from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('add/', monitor_add, name="monitor add"),
    path('details/<slug:monitor_name>/', monitor_details, name="monitor details"),
    path('edit/<slug:monitor_name>/', monitor_edit, name="monitor edit"),
    path('delete/<slug:monitor_name>/', monitor_delete, name="monitor delete"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)