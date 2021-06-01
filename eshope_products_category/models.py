from django.db import models

# Create your models here.



class Product_categories(models.Model):
    title=models.CharField(max_length=150,verbose_name='نام دسته بندی')
    name=models.CharField(max_length=150,verbose_name='عنوان در url')
    #

    def __str__(self):
        return self.title


    class Meta:
        verbose_name='دسته بندی '
        verbose_name_plural='دسته بندی ها'