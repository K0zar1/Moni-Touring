from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("review/<int:monitor_id>/", add_review, name="review"),
    path("review/<slug:monitor_name>/edit/<int:review_id>/", review_edit, name="edit review"),
    path("review/<slug:monitor_name>/delete/<int:review_id>/", review_delete, name="delete review"),
]