"""
URL configuration for project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("thanks/", views.thanks, name="thanks"),
    path("orders/", views.orders_list, name="orders_list"),
    path("orders/<int:order_id>/", views.order_details, name="order_details"),
    path("reviews/", views.reviews, name="reviews_list"),
    path("reviews/create/", views.create_review, name="create_review"),
]
