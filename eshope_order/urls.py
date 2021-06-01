from django.urls import path

from eshope_order.views import add_user_order , open_user_order , delete_user_order , empty_order , cart_partial

urlpatterns = [
    path('add_user_order',add_user_order),
    path('order/open_user_order',open_user_order),
    path('order/empty',empty_order),
    path('cart_partial',cart_partial,name='cart_partial'),
    path('order/delete_order/<product_id>',delete_user_order),
]



