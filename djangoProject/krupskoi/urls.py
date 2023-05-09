from django.urls import path, re_path
from djangoProject.krupskoi.views import ListView
urlpatterns = [
    re_path(r"^(?P<api_name>[a-z]+)", ListView, name='hotel-objects'),
]