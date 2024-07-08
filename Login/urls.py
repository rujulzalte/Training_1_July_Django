from . import views
from django.urls import path

#app urls

urlpatterns = [
    path("",views.homepage),
    path("users",views.user),
    path("index", views.index),
    path("alldetails",views.alldetails),
    path("singleuser/<int:pk>",views.singleuser),
]
