from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(_('title'), max_length=255)
    price = models.IntegerField(_('price'))
    description = models.TextField(_('description'), blank=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        db_table = 'product'


class Image(models.Model):
    image = models.ImageField(_('image'), upload_to='products/image')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='image')
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
        db_table = 'image'


class Category(models.Model):
    title = models.CharField(_('title'),max_length=255)
    product = models.ManyToManyField(Product)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        db_table = 'category'