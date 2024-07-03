from . import views
from django.urls import path

#app urls

urlpatterns = [
    path("",views.homepage),
    path("users",views.user),
    path("index", views.index),
]
