from django.shortcuts import render
from .models import *
from Products.models import Cart
# Create your views here.
#



def OrderCreate(request):
    cart= Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                ProductinOrder.objects.create(order=order,
                                               product=product.product_name,
                                                price_per_item=product.product_price,
                                                quantity=product.product_quantity)
            cart.clear()
            return render(request, )
