from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='notice'),
    path('new/', views.boardform, name="new"),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/remove/', views.remove, name='remove'),
    path('<int:board_id>', views.detail, name="detail"),
]