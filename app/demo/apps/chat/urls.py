from django.urls import path

from . import views


app_label = "chat"


urlpatterns = [
    path("", views.index),
    path("room/", views.room, name="room"),
]
