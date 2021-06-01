from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from eshope_products.models import Products


class Order(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    is_paied=models.BooleanField(verbose_name='پرداخت شده/نشده')
    payment_date=models.DateTimeField(blank=True,null=True,verbose_name='تاریخ پرداخت')


    class Meta:
        verbose_name='سبد خرید '
        verbose_name_plural='سبد های خرید کاربران'

    def __str__(self):
        return self.owner.get_full_name()




class OrderDetail(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name='سبد خرید')
    product=models.ForeignKey(Products,on_delete=models.CASCADE,verbose_name='محصول')
    price=models.IntegerField(verbose_name='قیمت')
    count=models.IntegerField(verbose_name='تعداد')


    class Meta:
        verbose_name='جزییات محصول'
        verbose_name_plural='اطلاعات جزییات محصول'

    def __str__(self):
        return self.product.title

    def get_product_url(self):
        return f'order/delete_order/{self.product_id}'
