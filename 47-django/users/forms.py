"""
users/forms.py
"""

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ValidationError
from django import forms
from .models import CustomUser


class UserLoginForm(AuthenticationForm):
    """
    login form
    """

    class Meta:
        model = CustomUser

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({"class": "form-control"})
        print(self.fields.keys())

class UserRegistrationForm(UserCreationForm):
    """
    registration form
    """

    class Meta:
        model = CustomUser
        fields = ["username", "password1", "password2", "email"]

    email = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}), required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({"class": "form-control"})
        print(self.fields.keys())

    def clean_email(self):
        """
        iterates through User instances
        """

        email = self.cleaned_data["email"]

        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с таким email уже зарегестрирован")

        return email

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user
