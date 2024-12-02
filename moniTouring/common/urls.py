from django.urls import path
from .views import index, share_link

urlpatterns = [
    path("", index, name="index"),
    path("share/<slug:recipe_name>/", share_link, name="share"),
]