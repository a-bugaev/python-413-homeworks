"""
URL configuration for project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.urls import path
from .views import (
    LandingView,
    ThanksView,
    OrdersListView,
    OrderDetailView,
    ReviewsView,
    ReviewCreateView,
)

urlpatterns = [
    path("", LandingView.as_view(), name="landing"),
    path("thanks/", ThanksView.as_view(), name="thanks"),
    path("orders/", OrdersListView.as_view(), name="orders_list"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order_details"),
    path("reviews/", ReviewsView.as_view(), name="reviews_list"),
    path("reviews/create/", ReviewCreateView.as_view(), name="create_review"),
]
