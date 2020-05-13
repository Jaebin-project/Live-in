from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="health_diary"),
    path('new/', views.postform, name="new"),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/remove/', views.remove, name='remove'),
    path('<int:post_id>', views.detail, name="detail"),
]