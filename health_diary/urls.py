from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="health_diary"),
    path('write/', views.postform, name="write"),
    path('<int:pk>/recontent/', views.edit, name='recontent'),
    path('<int:pk>/delete/', views.remove, name='delete'),
    path('<int:post_id>', views.detail, name="content"),
    # path('<int:comment_id>/edit_comment/', views.edit_comment, name='edit_comment'),
    path('<int:comment_id>/remove_comment/', views.remove_comment, name='remove_comment_hd'),
]