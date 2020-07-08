from django.urls import path
from . import views

app_name = "shorterurl"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:shorter_url>/", views.redirect_url, name="redirect_url"),
]
