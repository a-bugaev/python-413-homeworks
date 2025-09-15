"""
core/views.py
"""

import json

from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
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


class LandingView(TemplateView):
    """
    Landing page
    """

    template_name = "landing.html"
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("thanks")

    def __init__(self):
        self.order_form = OrderForm()

    def make_additional_json(self):
        """
        костыль для формы заявки
        """

        masters_services_py = []
        for master_obj in self.order_form.fields["master"].queryset:
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
        return json.dumps(masters_services_py, indent=4, ensure_ascii=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            **context,
            **{
                "masters": Master.objects.all(),
                "services": Service.objects.all(),
                "reviews": Review.objects.select_related("master")
                .prefetch_related("services_were_provided")
                .all(),
                "interior_pic": DecorImage.objects.get(name="interior").image,
                "order_form": self.order_form,
                "masters_services_json": self.make_additional_json(),
            },
        }
        return context

    def post(self, request, *args, **kwargs):
        """
        Обработка формы заявки
        """
        self.order_form = OrderForm(request.POST)
        if self.order_form.is_valid():
            self.order_form.save()
            messages.info(self.request, "Ваша заявка отправлена")
            return HttpResponseRedirect(reverse_lazy("thanks"))

        return self.render_to_response(self.get_context_data())


class ThanksView(TemplateView):
    """
    Thanks page
    """

    template_name = "thanks.html"


class OrdersListView(LoginRequiredMixin, ListView):
    """
    Orders list page
    """

    model = Order
    template_name = "orders_list.html"
    context_object_name = "orders"
    login_url = "login"

    def get_queryset(self):
        q_text = self.request.GET.get("q_text", "")
        checkbox_client_name = self.request.GET.get("checkbox_client_name", False)
        checkbox_phone = self.request.GET.get("checkbox_phone", False)
        checkbox_comment = self.request.GET.get("checkbox_comment", False)

        if q_text:
            query = Q()
            if checkbox_client_name:
                query |= Q(client_name__icontains=q_text)
            if checkbox_phone:
                query |= Q(phone__icontains=q_text)
            if checkbox_comment:
                query |= Q(comment__icontains=q_text)

            orders = (
                Order.objects.select_related("master").prefetch_related("services").filter(query)
            )
        else:
            orders = Order.objects.select_related("master").prefetch_related("services").all()

        return orders.order_by("-date_created")


class OrderDetailView(LoginRequiredMixin, DetailView):
    """
    Order details page
    """

    model = Order
    template_name = "order_details.html"
    context_object_name = "order"
    login_url = "login"

    def get_queryset(self, ):
        return (
            Order.objects.select_related("master")
            .prefetch_related("services")
            .annotate(total_price=Sum("services__price")).all()
        )


class ReviewsView(LoginRequiredMixin, TemplateView):
    """
    Reviews page
    """

    template_name = "reviews.html"


class ReviewCreateView(LoginRequiredMixin, CreateView):
    """
    Форма отзыва
    """

    model = Review
    form_class = ReviewForm
    template_name = "forms/create_review.html"
    success_url = reverse_lazy("thanks")

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "Ваш отзыв отправлен")
        super().form_valid(form)
        return HttpResponseRedirect(self.success_url)
