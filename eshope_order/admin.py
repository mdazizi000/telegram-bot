from django.contrib import admin

# Register your models here.
from eshope_order.models import Order, OrderDetail

admin.site.register(Order)
admin.site.register(OrderDetail)
