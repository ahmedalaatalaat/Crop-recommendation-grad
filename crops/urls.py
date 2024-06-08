from django.urls import path
from . import views

app_name = "crops"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.user_login, name="login"),
    path("registration/", views.user_registration, name="registration"),
    path("logout/", views.user_logout, name="logout"),
]