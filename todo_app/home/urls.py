from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="logn"),
    path('register', views.register, name="reg"),
    path('logout', views.logout, name="logout"),
]
