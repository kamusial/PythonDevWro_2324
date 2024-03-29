from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name="registration"),
    path("login", views.login, name="user-login"),
    path("logout", views.logout, name="user-logout"),
]
