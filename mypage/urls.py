from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="mypage"),
    path('add', views.addTodo, name="add"),
    path('delete', views.delete, name="delete"),
]