from django.urls import path
from . import views


app_name = "User"

urlpatterns = [
    path("logout/", views.log_out, name="logout"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("<int:pk>/", views.ProfileView.as_view(), name="profile"),
]
