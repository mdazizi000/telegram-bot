from django.urls import path
from .views import products_list , product_ditails , products_list_by_category,products_list_by_cheepest,products_list_by_newest,products_list_by_mostvisited,products_list_by_mostexpensive

urlpatterns = [

    path('products' , products_list.as_view()),
    path('products/mostvisited' , products_list_by_mostvisited.as_view()),
    path('products/cheepest' , products_list_by_cheepest.as_view()),
    path('products/newest' , products_list_by_newest.as_view()),
    path('products/mostexpensive' , products_list_by_mostexpensive.as_view()),
    path('products/<category_name>' , products_list_by_category.as_view()),
    path('products/<product_id>/<name>' ,product_ditails)


]