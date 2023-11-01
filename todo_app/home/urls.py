from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="logn"),
    path('register', views.register, name="reg"),
    path('logout', views.logout, name="logout"),
    path('home', views.index, name="list"),
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete")
]
