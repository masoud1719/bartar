from django.urls import path, include
from . import views

app_name = "bartarBase"
urlpatterns = [
    path("", views.index, name="homepage")
]
