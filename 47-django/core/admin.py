"""
register your models here
"""

from datetime import date, timedelta
import re

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models import Sum, Q, Count
from .models import (
    Order,
    Master,
    Service,
    Review,
)


class AppointmentFilter(admin.SimpleListFilter):
    title = "appointment_filter"
    parameter_name = "Клиент ожидается"

    def lookups(self, request, model_admin):
        return (("today", "Сегодня"), ("tomorrow", "Завтра"), {"this_week", "На этой неделе"})

    def queryset(self, request, queryset):
        if self.value() == "today":
            return queryset.filter(
                Q(appointment_date__gte=date.today())
                & Q(appointment_date__lt=date.today() + timedelta(days=1))
            )
        if self.value() == "tomorrow":
            return queryset.filter(
                Q(appointment_date__gte=date.today() + timedelta(days=1))
                & Q(appointment_date__lt=date.today() + timedelta(days=2))
            )
        if self.value() == "this_week":
            start_of_week = date.today() - date.today().weekday()
            end_of_week = start_of_week + timedelta(days=6)
            return queryset.filter(
                Q(date_field__gte=start_of_week) & Q(date_field__lte=end_of_week)
            )


class ServiceInline(admin.TabularInline):
    model = Order.services.through
    extra = 1

class OrderAdmin(ModelAdmin):
    list_display = [
        "id",
        "client_name",
        "phone",
        "master",
        "total_price",
        "status",
        "appointment_date",
    ]

    def get_queryset(self, request):
        # кастомный столбец с суммой заказа
        qs = super().get_queryset(request)
        qs = qs.annotate(total_price=Sum("services__price"))
        return qs

    @admin.display(description="Полная стоимость")
    def total_price(self, obj):
        return obj.total_price

    list_filter = [
        "status",
        "master",
        AppointmentFilter,
    ]

    search_fields = [
        "client_name",
        "phone",
    ]

    list_editable = ["status"]

    actions = [
        "set_stutus_new",
        "set_stutus_confirmed",
        "set_stutus_cancelled",
        "set_stutus_completed",
    ]

    @admin.action(description="Сменить статус на 'новая'")
    def set_stutus_new(self, request, queryset):
        DESIRABLE_STATUS = "new"

        queryset.update(status=DESIRABLE_STATUS)
        self.message_user(
            request,
            f"{len(queryset)} заявок теперь имеют статус {Order.STATUS_CHOICES[DESIRABLE_STATUS]}",
        )

    @admin.action(description="Сменить статус на 'подтвержденная'")
    def set_stutus_confirmed(self, request, queryset):
        DESIRABLE_STATUS = "confirmed"

        queryset.update(status=DESIRABLE_STATUS)
        self.message_user(
            request,
            f"{len(queryset)} заявок теперь имеют статус {Order.STATUS_CHOICES[DESIRABLE_STATUS]}",
        )

    @admin.action(description="Сменить статус на 'отмененная'")
    def set_stutus_cancelled(self, request, queryset):
        DESIRABLE_STATUS = "cancelled"

        queryset.update(status=DESIRABLE_STATUS)
        self.message_user(
            request,
            f"{len(queryset)} заявок теперь имеют статус {Order.STATUS_CHOICES[DESIRABLE_STATUS]}",
        )

    @admin.action(description="Сменить статус на 'выполненная'")
    def set_stutus_completed(self, request, queryset):
        DESIRABLE_STATUS = "completed"

        queryset.update(status=DESIRABLE_STATUS)
        self.message_user(
            request,
            f"{len(queryset)} заявок теперь имеют статус {Order.STATUS_CHOICES[DESIRABLE_STATUS]}",
        )

    ordering = ["-appointment_date"]

    inlines = [ServiceInline]


admin.site.register(Order, OrderAdmin)


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0

class MasterAdmin(ModelAdmin):
    list_display = [
        "name",
        "experience",
        "is_active",
        "services_count"
    ]

    def get_queryset(self, request):
        # кастомный столбец с количеством услуг
        qs = super().get_queryset(request)
        qs = qs.annotate(services_count=Count("services_provided"))
        return qs

    @admin.display(description="Количество привязанных услуг")
    def services_count(self, obj):
        return obj.services_count

    list_filter = [
        "is_active",
        "services_provided"
    ]

    search_fields = [
        "name"
    ]

    inlines = [ReviewInline]

admin.site.register(Master, MasterAdmin)

class ServiceAdmin(ModelAdmin):
    list_display = [
        "name",
        "price",
        "duration",
        "is_popular",
    ]

    list_filter = [
        "is_popular",
    ]

    search_fields = [
        "name"
    ]

admin.site.register(Service, ServiceAdmin)


admin.site.register(Review)
