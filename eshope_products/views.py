from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

from eshope_order.forms import UserNewOrderForm
from .models import Products
# Create your views here.
from django.views.generic import ListView
from eshope_products_category.models import Product_categories
from eshope_Subcategory.models import Product_subcategories
class products_list(ListView):
    template_name = 'search.html'
    paginate_by = 12
    def get_queryset(self):
        return Products.objects.get_active_pro().order_by('?')

class products_list_by_mostvisited(ListView):
    template_name = 'search.html'
    paginate_by = 12
    def get_queryset(self):
        return Products.objects.get_active_pro().order_by('-seen')


class products_list_by_cheepest(ListView):
    template_name = 'search.html'
    paginate_by = 12

    def get_queryset(self):
        return Products.objects.get_active_pro().order_by('price')


class products_list_by_newest(ListView):
    template_name = 'search.html'
    paginate_by = 12

    def get_queryset(self):
        return Products.objects.get_active_pro().order_by('-date')


class products_list_by_mostexpensive(ListView):
    template_name = 'search.html'
    paginate_by = 12

    def get_queryset(self):
        return Products.objects.get_active_pro().order_by('-price')


def product_ditails(request,*args,**kwargs):
    product_id=kwargs['product_id']
    orderform = UserNewOrderForm(request.POST or None,initial={'product_id':product_id})
    product=Products.objects.get_by_id(product_id)
    if product is None or not product.active:
        return Http404("محصول مورد نظر یافت نشد")
    context={
        'product':product,
        'orderform':orderform
    }
    return render(request,'single-product.html',context)


class products_list_by_category(ListView):
    template_name = 'search.html'
    paginate_by = 12

    def get_queryset(self):
        category_name=self.kwargs['category_name']
        category=Product_categories.objects.filter(name__iexact=category_name)
        if category is None:
            raise Http404('دسته بندی مورد نظر یافت نشد')
        return Products.objects.get_by_categories(category_name)

