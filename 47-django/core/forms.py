"""
core/forms.py
"""

from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Order, Review, Master, Service


class ReviewForm(forms.ModelForm):
    """
    Форма отзыва
    """

    class Meta:
        model = Review
        fields = ("client_name", "text", "master", "rating")

    master: forms.ModelChoiceField = forms.ModelChoiceField(
        queryset=Master.objects.all(),  # pylint: disable=no-member
        empty_label="Мастер",
        label="Мастер",
    )

    rating = forms.IntegerField(
        label="Оценка",
        widget=forms.NumberInput(attrs={"min": 1, "max": 5, "class": "form-control"}),
        validators=[MinValueValidator(Review.RATING_MIN), MaxValueValidator(Review.RATING_MAX)],
    )


class OrderForm(forms.ModelForm):
    """
    Форма заявки
    """

    class Meta:
        model = Order
        fields = ("client_name", "phone", "master", "services", "comment")

    client_name: forms.CharField = forms.CharField(
        label="Имя клиента"
    )

    master: forms.ModelChoiceField = forms.ModelChoiceField(
        queryset=Master.objects.all(),  # pylint: disable=no-member
        empty_label="Мастер",
        label="Мастер",
    )

    services: forms.ModelMultipleChoiceField = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(), label="Услуги"  # pylint: disable=no-member
    )

    def clean(self):
        cleaned_data = super().clean()

        master = cleaned_data.get("master")
        services = cleaned_data.get("services")

        if master and services:
            available_services = master.services_provided.all()
            for service in services:
                if service not in available_services:
                    raise forms.ValidationError(
                        f"Мастер {master.name} не предоставляет услугу {service.name}"
                    )

        return cleaned_data
