from django.urls import path
from . import views

app_name = "shorterurl"

urlpatterns = [
    path("", views.index, name="index"),
    # path('<str:token>', views.index, name='index'),
]
