"""
core/views.py
"""

from django.shortcuts import render
from django.db.models import Q, Sum
from .models import (
    Order,
    Master,
    Service,
    Review,
    DecorImage,
)

# pylint: disable=no-member


def landing(request):
    """
    Landing page
    """

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
                .annotate(total_price=Sum("services__price")).get(id=order_id)
            },
        )
    return render(request, "403.html")
