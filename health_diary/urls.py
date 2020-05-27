from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="health_diary"),
    path('new/', views.postform, name="new_hd"),
    path('<int:pk>/edit/', views.edit, name='edit_hd'),
    path('<int:pk>/remove/', views.remove, name='remove_hd'),
    path('<int:post_id>', views.detail, name="detail_hd"),
    # path('<int:comment_id>/edit_comment/', views.edit_comment, name='edit_comment'),
    path('<int:comment_id>/remove_comment/', views.remove_comment, name='remove_comment_hd'),
]