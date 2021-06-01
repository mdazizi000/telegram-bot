from django.urls import path
from .views import get_subcat
urlpatterns = [
    path('subcatpartial' ,get_subcat , name='subcatpartial' )
]