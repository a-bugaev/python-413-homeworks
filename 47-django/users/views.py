"""
users/views.py
"""

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserLoginForm, UserRegistrationForm


class UserLoginView(LoginView):
    """
    страница входа
    """

    form_class = UserLoginForm
    template_name = "login_registration.html"

    def get_context_data(self, **kwargs):
        """
        констекст шаблона
        """
        context = super().get_context_data(**kwargs)
        context = {**context, **{"title": "Вход", "button_text": "Войти"}}
        return context


class UserRegistrationView(CreateView):
    """
    страница регистрации
    """

    form_class = UserRegistrationForm
    template_name = "login_registration.html"
    success_url = reverse_lazy("landing")

    def get_context_data(self, **kwargs):
        """
        констекст шаблона
        """
        context = super().get_context_data(**kwargs)
        context = {**context, **{"title": "Регистрация", "button_text": "Зарегестрироваться"}}
        return context


class UserLogoutView(LogoutView):
    """
    не видна пользователю
    """
