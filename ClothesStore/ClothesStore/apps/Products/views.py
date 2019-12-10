from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse, JsonResponse
from .models import *
from django.urls import reverse
from Users.models import SimpleUser
from decimal import Decimal

def index(request):
    # list_products = Product.objects.order_by("-created")[:5]
    # all_list_products = Product.objects.order_by("-id")[:20]
    list_products=ProductImage.objects.filter(is_active=True, is_main=True, product__available=True)
    list_products_outerwear = list_products.filter(product__category__id=7)
    context={'list_products':list_products ,
             'lpo': list_products_outerwear,
             }
    # popular_products = Like.objects.filter(heart_click__gt=3).order_by('-heart_click')[:4]
    # art = get_object_or_404(Product, pk=article_id)
    # art.numberOfClicks +=1
    # art.save()
    return render(request, 'index.html', context)
# 'popular_products'=popular_products

def detail(request, product_id):
    try:
        a=Product.objects.get(id= product_id)
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
        raise Http404("Page is not found!")
    list_comments=a.comment_set.order_by('-comment_pub_date')[:10]
    context= {'cart': cart,
              'list_products':a,
              'list_comments':list_comments,
              }
    return render(request,'detail.html', context)

def leave_comment(request, product_id):
    if request.method == 'POST':
        try:
            a=Product.objects.get(id=product_id)
        except:
            raise Http404("Product didn`t find")
        a.comment_set.create(author_name = SimpleUser.objects.get(username = request.POST['username']), comment_text = request.POST['comments_text'])
        a.save()
    return HttpResponseRedirect(reverse('Products:detail' , args=(a.id,)))




def search(request,product_name):
    search_byname=list(Product.objects.filter(product_name__contains=product_name).values_list('product_name'))
    # search_bysize=list(Product.objects.filter(product_size__contains=product_size).values_list('product_size'))
    # search_bybrand=list(Product.objects.filter(product_brand__contains=product_brand).values_list('product_brand'))
    # search_byname=list(Product.objects.filter(product_price__contains=product_price).values_list('product_price'))
    try:
        products =""
        print("We are here", search_byname)
        for i in search_byname:
            print(*i)
            products= products + "<h3>%i: "%(search_byname.index(i)+1) + "</h3><br>"
            print(products)
        return HttpResponse("<h2>This is the resoult of search</h2> %s" % products)
    except:
        return HttpResponse("No such products")

def base_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id=cart.id
        request.session['cart_id'] = cart_id
        cart=Cart.objects.get(slug=product_slug)
    context = {
               'cart':cart
               }
    return render(request, 'base.html', context)



def cart_view(request):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)

	# product = Product.objects.get(slug=product_slug)

	context= {
	# 'category': category,
	'cart': cart,
	# 'product': product,
	}

	return render(request, 'cart.html', context)

def add_to_cart_view(request):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)

	product_slug = request.GET.get('product_slug')
	product = Product.objects.get(slug=product_slug)
	cart.add_to_cart(product.slug)

	# ИТОГОВЫЙ ЦЕНА
	new_cart_total =0.00
	for item in cart.items.all():
		new_cart_total += float(item.item_total)
	cart.cart_total = new_cart_total
	cart.save()

	return JsonResponse({'cart_total': cart.items.count(),'cart_total_price': cart.cart_total})


def remove_from_cart_view(request):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)


	product_slug = request.GET.get('product_slug')
	product = Product.objects.get(slug=product_slug)
	cart.remove_from_cart(product.slug)

	# ИТОГОВЫЙ ЦЕНА
	new_cart_total =0.00
	for item in cart.items.all():
		new_cart_total += float(item.item_total)
	cart.cart_total = new_cart_total
	cart.save()


	return JsonResponse({'cart_total': cart.items.count(),'cart_total_price': cart.cart_total})

def change_item_qty(request):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)

	qty = request.GET.get('qty')
	item_id = request.GET.get('item_id')
	# print(qty, item_id)
	cart_item = CartItem.objects.get(id=int(item_id))
	cart_item.qty = int(qty)
	cart_item.item_total = int(qty) * Decimal(cart_item.product.price)
	cart_item.save()

	# ИТОГОВЫЙ ЦЕНА
	new_cart_total =0.00
	for item in cart.items.all():
		new_cart_total += float(item.item_total)
	cart.cart_total = new_cart_total
	cart.save()

	return JsonResponse(
		{'cart_total': cart.items.count(),
		'item_total': cart_item.item_total,
		'cart_total_price': cart.cart_total
		})



# def cart_view(request):
#     try:
#         cart_id = request.session['cart_id']
#         cart = Cart.objects.get(id=cart_id)
#         request.session['total'] = cart.items.count()
#     except:
#         cart = Cart()
#         cart.save()
#         cart_id = cart.id
#         request.session['cart_id'] = cart_id
#         cart = Cart.objects.get(id=cart_id)
#     context = {
#                'cart':cart
#     }
#     return render(request, 'cart.html', context)
#
# def add_to_cart_view(request):
# 	try:
# 		cart_id = request.session['cart_id']
# 		cart = Cart.objects.get(id=cart_id)
# 		request.session['total'] = cart.items.count()
# 	except:
# 		cart = Cart()
# 		cart.save()
# 		cart_id = cart.id
# 		request.session['cart_id'] = cart_id
# 		cart = Cart.objects.get(id=cart_id)
#
# 	product_slug = request.GET.get('product_slug')
# 	product = Product.objects.get(slug=product_slug)
# 	cart.add_to_cart(product.slug)
#
# 	# ИТОГОВЫЙ ЦЕНА
# 	new_cart_total =0.00
# 	for item in cart.items.all():
# 		new_cart_total += float(item.item_total)
# 	cart.cart_total = new_cart_total
# 	cart.save()
#
# 	return JsonResponse({'cart_total': cart.items.count(),'cart_total_price': cart.cart_total})
#
#
#     # def add_to_card_view(request, product_slug):
#     #     product=product.objects.get(slug = product_slug)
#     #     new_item_=CartItem.objects.get_or_create(product=product_name, item_total=product.product_price)
#     #     cart=Cart.objects.first()
#     #     if new_item.add(new_item):
#     #         cart.save()
#     #     return HttpResponseRedirect('/cart/')
#
#     # def remove_from_cart(self,product_slug):
# 	# 	cart = self
# 	# 	product = Product.objects.get(slug=product_slug)
#     #
# 	# 	for cart_item in cart.items.all():
# 	# 		if cart_item.product == product:
# 	# 			cart.items.remove(cart_item)
# 	# 			cart.save()
# 	# 			return HttpResponseRedirect('/cart/')
# def remove_from_cart_view(request):
#     try:
#         cart_id = request.session['cart_id']
#         cart = Cart.objects.get(id=cart_id)
#         request.session['total'] = cart.items.count()
#     except:
#         cart = Cart()
#         cart.save()
#         cart_id = cart.id
#         request.session['cart_id'] = cart_id
#         cart = Cart.objects.get(id=cart_id)
#
#     product_slug = request.GET.get('product_slug')
#     product = Product.objects.get(slug=product_slug)
#     cart.add_to_cart(product.slug)
#     # ИТОГОВЫЙ ЦЕНА
#     new_cart_total =0.00
#     for item in cart.items.all():
#         new_cart_total += float(item.item_total)
#     cart.cart_total = new_cart_total
#     cart.save()
#     return JsonResponse({'cart_total': cart.items.count(),'cart_total_price': cart.cart_total})
#
# # def change_item_qty(request):
# #     try:
# #         cart_id = request.session['cart_id']
# #         cart = Cart.objects.get(id=cart_id)
# #         request.session['total'] = cart.items.count()
# #     except:
# #         cart = Cart()
# #         cart.save()
# #         cart_id = cart.id
# #         request.session['cart_id'] = cart_id
# #         cart = Cart.objects.get(id=cart_id)
# #
# #     qty = request.GET.get('qty')
# #     item_id = request.GET.get('item_id')
# #     # print(qty, item_id)
# #     cart_item = CartItem.objects.get(id=int(item_id))
# #     cart_item.qty = int(qty)
# #     cart_item.item_total = int(qty) * Decimal(cart_item.product.price)
# #     cart_item.save()
# #
# #     # ИТОГОВЫЙ ЦЕНА
# #     new_cart_total =0.00
# #     for item in cart.items.all():
# #         new_cart_total += float(item.item_total)
# #     cart.cart_total = new_cart_total
# #     cart.save()
# #     return JsonResponse({
# #                          'cart_total': cart.items.count(),
# #                          'item_total': cart_item.item_total,
# #                          'cart_total_price': cart.cart_total
# #                          })
