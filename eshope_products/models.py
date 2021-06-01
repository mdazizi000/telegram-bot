import os

from django.db import models
from django.utils import timezone

from eshope_products_category.models import Product_categories
from eshope_Subcategory.models import Product_subcategories
# Create your models here.\
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"
class ProductsManager(models.Manager):
    def get_active_pro(self):
        return self.get_queryset().filter(active=True)
    def get_by_id(self,product_id):
        qs=self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()

    def get_by_categories(self,category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name)

class Products(models.Model):
    title=models.CharField(max_length=100,verbose_name='نام محصول')
    price=models.IntegerField(verbose_name='قیمت')
    discription=models.TextField(verbose_name='توضیحات',null=True,blank=True)
    brand=models.CharField(max_length=50,verbose_name='برند')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True,verbose_name='تصویر')
    active=models.BooleanField(default=False,verbose_name='فعال/غیر فعال')
    seen=models.IntegerField(default=0,verbose_name='بازدید فیک')
    categories=models.ManyToManyField(Product_categories,blank=True,verbose_name='دسته بندی')
    subcategories=models.ManyToManyField(Product_subcategories,blank=True,verbose_name='زیردسته بندی')
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name='محصول'
        verbose_name_plural='محصولات'
    def get_absolut_url(self):
        return f"/products/{self.id}/{self.title}"
    def get_mostvisited_url(self):
        return "/products/mostvisited"
    def get_cheepest_url(self):
        return "/products/cheepest"

    objects=ProductsManager()