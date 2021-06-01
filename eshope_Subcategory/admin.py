from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product_subcategories

# Register your models here.
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'name']

admin.site.register(Product_subcategories,ProductCategoryAdmin)