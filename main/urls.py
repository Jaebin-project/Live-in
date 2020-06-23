from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name="main"),
    path('login/', views.login, name="login"),
    path('new_user/', views.new_user, name="new_user"),
]