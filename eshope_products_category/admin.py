from django.contrib import admin
from .models import Product_categories

# Register your models here.
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'name']

admin.site.register(Product_categories,ProductCategoryAdmin)