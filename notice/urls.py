from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='notice'),
    path('new/', views.boardform, name="new"),
    path('new_pro/', views.proboardform, name="new_pro"),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/remove/', views.remove, name='remove'),
    path('<int:board_id>', views.detail, name="detail"),
    path('<int:comment_id>/remove_comment/', views.remove_comment, name='remove_comment'),
]