from . import views
from django.urls import path

#app urls

urlpatterns = [
    path("homepage/",views.homepage),
    path("homepage/users",views.user),
]
