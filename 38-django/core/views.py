"""
core/views.py
"""

from django.shortcuts import render
from core.test_data import (
    MASTERS,
    SERVICES,
    ORDERS,
    get_master_ids,
    get_service_ids,
    get_order_by_id,
    get_master_by_id,
    get_service_by_id,
)


def landing(request):
    """
    Landing page
    """
    masters_imgs = {id_: f"/static/img/master/{id_}.webp" for id_ in get_master_ids()}
    services_imgs = {id_: f"/static/img/service/{id_}.webp" for id_ in get_service_ids()}

    context = {
        "masters": MASTERS,
        "services": SERVICES,
        "masters_imgs": masters_imgs,
        "services_imgs": services_imgs,
    }
    return render(request, "landing.html", context=context)


def thanks(request):
    """
    Thanks page
    """
    return render(request, "thanks.html")


def orders_list(request):
    """
    Orders list page
    """

    orders = ORDERS
    masters = MASTERS
    services = SERVICES

    context = {"orders": orders, "masters": masters, "services": services}

    return render(request, "orders_list.html", context=context)


def order_details(request, order_id):
    """
    Order details page

    structure:
    "id": 1,
    "client_name": "Пётр 'Безголовый' Головин",
    "services": [1, 10],
    "master_id": 1,
    "date": "2025-03-20",
    "status": STATUS_NEW,
    """

    order = get_order_by_id(order_id)
    master = get_master_by_id(order["master_id"])
    services = []
    for service in order["services"]:
        services.append(get_service_by_id(service))

    context = {
        "order": order,
        "master": master,  # master of order
        "services": services,  # service objects of order
    }

    return render(request, "order_details.html", context=context)
