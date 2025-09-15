"""
core/views.py
"""

import json

from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.models import Q, Sum
from .models import (
    Order,
    Master,
    Service,
    Review,
    DecorImage,
)
from .forms import ReviewForm, OrderForm

# pylint: disable=no-member


def landing(request):
    """
    Landing page
    """

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Ваша заявка отправлена')
            return redirect("thanks")
    else:
        form = OrderForm()

    masters_services_py = []
    for master_obj in form.fields["master"].queryset:
        masters_services_py.append(
            {
                "master_id": master_obj.id,
                "master_name": master_obj.name,
                "master_services": [
                    {
                        "service_id": service.id,
                        "service_name": service.name,
                    }
                    for service in master_obj.services_provided.all()
                ],
            }
        )
    masters_services_json = json.dumps(masters_services_py, indent=4, ensure_ascii=False)

    return render(
        request,
        "landing.html",
        context={
            "masters": Master.objects.all(),
            "services": Service.objects.all(),
            "reviews": Review.objects.select_related("master")
            .prefetch_related("services_were_provided")
            .all(),
            "interior_pic": DecorImage.objects.get(name="interior").image,
            "order_form": form,
            "masters_services_json": masters_services_json,
        },
    )


def thanks(request):
    """
    Thanks page
    """
    return render(request, "thanks.html")


def orders_list(request):
    """
    Orders list page
    """

    q_text = request.GET.get("q_text", "")
    checkbox_client_name = request.GET.get("checkbox_client_name", False)
    checkbox_phone = request.GET.get("checkbox_phone", False)
    checkbox_comment = request.GET.get("checkbox_comment", False)

    if q_text:
        query = Q()
        if checkbox_client_name:
            query |= Q(client_name__icontains=q_text)
        if checkbox_phone:
            query |= Q(phone__icontains=q_text)
        if checkbox_comment:
            query |= Q(comment__icontains=q_text)

        orders = Order.objects.select_related("master").prefetch_related("services").filter(query)
    else:
        orders = Order.objects.select_related("master").prefetch_related("services").all()

    orders = orders.order_by("-date_created")

    if request.user.is_authenticated:
        return render(
            request,
            "orders_list.html",
            context={
                "orders": orders,
            },
        )
    return render(request, "403.html")


def order_details(request, order_id):
    """
    Order details page
    """

    if request.user.is_authenticated:
        return render(
            request,
            "order_details.html",
            context={
                "order": Order.objects.select_related("master")
                .prefetch_related("services")
                .annotate(total_price=Sum("services__price"))
                .get(id=order_id)
            },
        )
    return render(request, "403.html")


def reviews(request):
    """
    форму отзыва надо куда-то засунуть :(
    """
    return render(request, "reviews.html")


def create_review(request):
    """
    Форма отзыва
    """
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Ваш отзыв отправлен')
            return redirect("thanks")
    else:
        form = ReviewForm()

    return render(request, "forms/create_review.html", {"form": form})
