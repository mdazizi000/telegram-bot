from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from eshope_products.models import Products
from .forms import UserNewOrderForm
# Create your views here.
from eshope_order.models import Order, OrderDetail


@login_required
def add_user_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)

    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paied=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paied=False)

        product_id = new_order_form.cleaned_data.get('product_id')

        product = Products.objects.get_by_id(product_id=product_id)
        order.orderdetail_set.create(product_id=product.id, price=product.price, count=1)
        # todo: redirect user to user panel
        # return redirect('/user/orders')
        return redirect(f'/products/{product.id}/{product.title.replace(" ", "-")}')

    return redirect('/')


@login_required(login_url='/login')
def open_user_order(request):
    total = 0
    count = 0
    context = {
        'order': None,
        'details': None,
        'total': total,
        'count': count
    }

    open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paied=False).first()
    if open_order is not None:
        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()
    order1 = open_order.orderdetail_set.all()
    order2 = bool(order1)
    if order2 is False:
        return redirect('/order/empty')

    for detail in order1:
        total += detail.product.price
        count += 1
    context['total'] = total
    context['count'] = count
    return render(request, 'cart.html', context)


def delete_user_order(request, *args, **kwargs):
    product_id = kwargs['product_id']
    total = 0
    count = 0
    context = {
        'order': None,
        'details': None,
        'total': total,
        'count': count
    }

    open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paied=False).first()
    open_order.orderdetail_set.filter(product_id=product_id).delete()
    if open_order is not None:
        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()

    order1 = open_order.orderdetail_set.all()

    order2 = bool(order1)
    if order2 is False:
        return redirect('/order/empty')


    for detail in order1:
            total += detail.product.price
            count += 1
            context['total'] = total
            context['count'] = count

    return render(request, 'cart.html', context)


def empty_order(request):
    return render(request, 'cart-empty.html', {})


def cart_partial(request):
    # total = 0
    # count = 0
    # context = {
    #     'order': None,
    #     'details': None,
    #     'total': total,
    #     'count': count
    # }
    #
    # open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paied=False).first()
    #
    # if open_order is not None:
    #     context['order'] = open_order
    #     context['details'] = open_order.orderdetail_set.all()
    #
    # order1 = open_order.orderdetail_set.all()
    #
    # for detail in order1:
    #     total += detail.product.price
    #     count += 1
    # context['total'] = total
    # context['count'] = count
    return render(request, 'cart_partial.html', {})
