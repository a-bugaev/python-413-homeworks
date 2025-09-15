"""
core/signals.py
"""

from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Order
from .telegram_bot_script import send_message, escape_md2


@receiver(m2m_changed, sender=Order.services.through)  # pylint: disable=no-member
def send_telegram_notification(
    sender, instance, action, **kwargs
):  # pylint: disable=unused-argument
    """
    telegram notification about new order
    """
    if action != "post_add":
        return
    name = escape_md2(instance.client_name)
    phone = escape_md2(instance.phone)
    master = escape_md2(instance.master.name)
    services = escape_md2("\n".join([service_obj.name for service_obj in instance.services.all()]))
    appointment_date = escape_md2(instance.appointment_date.strftime("%Y-%m-%d %H:%M"))
    message_text = f"""
        *НОВЫЙ ЗАКАЗ*
        *Клиент:*
        {name}
        *Номер:*
        {phone}
        *Мастер:*
        {master}
        *Услуги:*
        {services}
        *Дата и время:*
        {appointment_date}
    """.replace(
        "    ", ""
    )
    send_message(message_text)
