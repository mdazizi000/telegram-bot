from django.contrib import admin
from .models import Products
# Register your models here.
class ProdutsAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'active','price','brand']
admin.site.register(Products,ProdutsAdmin)