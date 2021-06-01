from django.shortcuts import render,redirect
from eshope_products_category.models import Product_categories
def page_home(request):
    return render(request,'index.html' , {})


def headre_partial(request):
    category=Product_categories.objects.all()
    context={
        'category':category
    }
    return render(request,'header_partial.html' ,context)