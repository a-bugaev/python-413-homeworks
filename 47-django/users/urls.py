"""
users/urls.py
"""

from django.urls import path
from .views import (
    UserLoginView,
    UserRegistrationView,
    UserLogoutView,
)

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]
