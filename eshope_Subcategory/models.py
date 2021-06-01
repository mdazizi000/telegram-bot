from django.db import models
from eshope_products_category.models import Product_categories
# Create your models here.
from django.db import models

# Create your models here.
class ProductsAdmin(models.Manager):
    def get_by_subcat(self,subcategory_name):
        return self.get_queryset().filter(subcategories__name__iexact=subcategory_name)

class Product_subcategories(models.Model):
    subcategories=models.ManyToManyField(Product_categories,blank=True,verbose_name="دسته بندی اصلی")
    title=models.CharField(max_length=150,verbose_name='نام زیردسته بندی')
    name=models.CharField(max_length=150,verbose_name='عنوان در url')


    objects=ProductsAdmin()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name='زیردسته بندی '
        verbose_name_plural=' زیردسته بندی ها'