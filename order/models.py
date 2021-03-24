from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Order_list(models.Model):
    SUCCESS = 1
    PROGRESS = 2
    CANCELL = 3
    STATUS_CHOICE = (
        (SUCCESS, 'Success'),
        (PROGRESS, 'Progress'),
        (CANCELL, 'Cancell')
    )
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='user_order')
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='product_order')
    status = models.SmallIntegerField(_('status'), choices=STATUS_CHOICE,default=PROGRESS)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')
        db_table = _('order')